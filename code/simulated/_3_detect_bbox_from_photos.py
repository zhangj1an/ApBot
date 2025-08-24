# object detector 
from PIL import Image

import copy
import _0_t2a_config
from foundation_models.owlv2_crane5_query import OWLViT, visualize_image, filter_bboxes, format_label
from foundation_models.fastsam_model import fast_sam
from utils.create_or_replace_path import create_or_replace_path
from utils.crop_image import crop_image_to_focus_on_bbox, convert_to_original_coords
from utils.ocr_detect_bounding_boxes import ocr_detect_bounding_boxes
from utils.color_code import bright_red, bright_green
from foundation_models.gpt_4o_model import GPT4O
from foundation_models.owlv2_anxing import OWLViT as OWLViT_anxing
import io
import json
import numpy as np
import os
import cv2
import easyocr
import torch
import math
import threading

owl_detector = OWLViT(server_url="http://crane5.d2.comp.nus.edu.sg:4229") # OWLViT_anxing()#
#intern_detector = InternVL()

def calculate_area(bbox):
    xmin, ymin, xmax, ymax = bbox
    width = xmax - xmin
    height = ymax - ymin
    return width * height

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated

def match_template(image, template, box_name, threshold=0.8):
    results = []
    for angle in [0, 90, 180, 270]:
        rotated_template = rotate_image(template, angle)
        result = cv2.matchTemplate(image, rotated_template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            bbox = [
                pt[0] / image.shape[1],
                pt[1] / image.shape[0],
                (pt[0] + rotated_template.shape[1]) / image.shape[1],
                (pt[1] + rotated_template.shape[0]) / image.shape[0]
            ]
            score = result[pt[1], pt[0]]
            results.append({
                "score": score,
                "bbox": bbox,
                "label": box_name
            })

    return results

def template_matching(image_path, template_dir="/data/home/jian/RLS_microwave/utils/_3_img_to_bbox/sample_icons"):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found.")

    all_results = []
    # list dir in template_dir  
    templates = [os.path.join(template_dir, file) for file in os.listdir(template_dir) if file.endswith(('.jpg', '.jpeg', '.png'))]
    for template_path in templates:
        box_name = template_path.split("/")[-1].split(".")[0]
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            raise FileNotFoundError(f"Template file '{template_path}' not found.")

        results = match_template(image, template, box_name)
        all_results.extend(results)

    return all_results

def crop_image_with_normalized_coords(raw_image, norm_coords):
    
    # Get the dimensions of the image
    img_width, img_height = raw_image.size
    
    # Convert normalized coordinates to pixel coordinates
    xmin = int(norm_coords[0] * img_width)
    ymin = int(norm_coords[1] * img_height)
    xmax = int(norm_coords[2] * img_width)
    ymax = int(norm_coords[3] * img_height)
    
    # Crop the image
    cropped_image = raw_image.crop((xmin, ymin, xmax, ymax))
    
    return cropped_image

def check_control_panel_validity(bbox_list, raw_image, machine_type, machine_id, pic_id, validity_save_path = "/data/home/jian/RLS_microwave/benchmark_3/_2_control_panel_images/_5_validity_control_panel", gpt_model_type = "gpt-4o"):
    
    prompt = """
    Does the red bounding box contain a control panel element (e.g., button, dial)? Note that in soft pad layouts, text labels printed on control panel can serve as a virtual button and responds to presses, providing interactive control. Therefore they should be considered a control panel element. Please include symbols like "+", "-", start, "on/off", numbers that appeared on the control panel region as valid too. If the red bounding box contain a control panel element, reply "Yes". If no, reply "No". Provide a reason as well, by naming the object being circled by the red bounding box. 
    """

    
    result_list = []
    total_len = len(bbox_list)
    for i, bbox in enumerate(bbox_list):
        # visualise a image with the bbox 
        if i % 1 == 0:
            print(f"processing the {i}/{total_len} th bbox")
        
        edited_image = visualize_image(raw_image, bboxes = [bbox["bbox"]], return_img=True, labels=None, show=False, rect_color=bright_red)
        edited_image,_ = crop_image_to_focus_on_bbox(edited_image, bbox["bbox"], 5)
        
        
        # save the image
        save_path = os.path.join(validity_save_path, machine_type, machine_id, pic_id)
        filename = f"{i}.png"
        full_path = os.path.join(save_path, filename)
 
        create_or_replace_path(full_path)
        edited_image.save(full_path)
        
        model = GPT4O()
        response = model.chat_with_multiple_images(prompt, [full_path], gpt_model_type, temperature=1, top_p=1)
        print(response)
        if any(s in response for s in ["Yes", "yes"]):
            result_list.append(bbox)
    return result_list

def get_union_bbox(bbox_list):
    if not bbox_list:
        return None

    # Initialize the union bbox with the first bbox in the list
    x_min, y_min, x_max, y_max = bbox_list[0]['bbox']

    for item in bbox_list[1:]:
        bbox = item['bbox']
        x_min = min(x_min, bbox[0])
        y_min = min(y_min, bbox[1])
        x_max = max(x_max, bbox[2])
        y_max = max(y_max, bbox[3])

    return [x_min, y_min, x_max, y_max]

def convert_to_cropped_coords(crop_coord, source_objects):
    detected_objects = copy.deepcopy(source_objects) 
    xmin_crop, ymin_crop, xmax_crop, ymax_crop = crop_coord
    crop_width = xmax_crop - xmin_crop
    crop_height = ymax_crop - ymin_crop

    cropped_coords_list = []

    for detected_object in detected_objects:
        xmin_obj, ymin_obj, xmax_obj, ymax_obj = detected_object["bbox"]
        
        # Convert coordinates from original image to cropped image
        xmin_cropped = (xmin_obj - xmin_crop) / crop_width
        ymin_cropped = (ymin_obj - ymin_crop) / crop_height
        xmax_cropped = (xmax_obj - xmin_crop) / crop_width
        ymax_cropped = (ymax_obj - ymin_crop) / crop_height

        detected_object["bbox"] = [xmin_cropped, ymin_cropped, xmax_cropped, ymax_cropped]
        cropped_coords_list.append(detected_object)
    
    return cropped_coords_list

def crop_out_control_panel(raw_image):
    text_queries = ["appliance"]
    det_data = owl_detector.detect_objects(
    image=raw_image,
    text_queries=text_queries,
    bbox_score_top_k=20, 
    bbox_conf_threshold=0.12 
    )  
    # [{'score': score, 'bbox': bbox, 'label': label}]
    bbox = get_union_bbox(det_data)

    return bbox

def process_image(image_path = "/data/home/jian/RLS_microwave/reasoning/rls_data/microwave/photo/0.jpg", bbox_savepath = None, detected_image_path = None, machine_type="", machine_id="", pic_id="", validity_save_path = "/data/home/jian/RLS_microwave/benchmark/control_panel_images_validity", gpt_model_type ="gpt-4o", require_ocr = True, sam_conf = 0.2, sam_iou = 0.1, text_queries = ["button", "digital display", "dial", "switch", "symbol", "icon", "arrow"]
):
    create_or_replace_path(detected_image_path)
    create_or_replace_path(bbox_savepath)

    raw_image = Image.open(image_path)

    #control_panel_bbox = crop_out_control_panel(raw_image)
    #if not control_panel_bbox:
    #    return 
    
    #cropped_control_panel_image = crop_image_with_normalized_coords(raw_image, control_panel_bbox)

    # save as a new image
    #cropped_control_panel_image_filepath = detected_image_path.replace(".png", "_control_panel.png")
    #cropped_control_panel_image.save(cropped_control_panel_image_filepath)

    # firstly, detect control panels using OWL, then only detect the bounding box from the cropped image 
    # retain the image rato between the cropped image and the original image
    # so that the detected bounding boxes can be mapped back to the original image
    det_data = []
    #det_data = owl_detector.detect_objects(
    #image=cropped_control_panel_image,
    #text_queries=text_queries,
    #bbox_score_top_k=20, 
    #bbox_conf_threshold=0.12 
    #)  

    # remove IoU 
    #det_data = filter_bboxes(det_data, threshold=0.2) 

    
    # add another portion about the OCR 
    if require_ocr:
        #ocr_data = ocr_detect_bounding_boxes(cropped_control_panel_image_filepath)
        ocr_data = ocr_detect_bounding_boxes(image_path)
        ocr_data = filter_bboxes(ocr_data, threshold=0.3)
        print("Number of OCR detected objects: ", len(ocr_data))
        det_data.extend(ocr_data)

    #sam_data = fast_sam(img_path=cropped_control_panel_image_filepath, iou=sam_iou, conf=sam_conf)
    sam_data = fast_sam(img_path=image_path, iou=sam_iou, conf=sam_conf)

    print("Number of OWL detected objects: ", len(det_data))
    
    print("Number of SAM detected objects: ", len(sam_data))

    # combine the two data 
    
    det_data.extend(sam_data)

    det_data = filter_bboxes(det_data, threshold=0.3)
    
    # now convert the det_data back to the original image 
    #det_data = convert_to_original_coords(control_panel_bbox, det_data)


    # delete the control panel image 
    #os.remove(cropped_control_panel_image_filepath)
    
    # here add code to filter off invalid bboxes that are not button, dial or digital displays
    print("validity save path in process image: ", validity_save_path)
    det_data = check_control_panel_validity(det_data, raw_image, machine_type, machine_id, pic_id, validity_save_path, gpt_model_type)
    print(det_data)
    
    annotated_image = visualize_image(raw_image, bboxes = [obj["bbox"] for obj in det_data], return_img=True, labels=[obj["label"] for obj in det_data], show=False) # display_label = "box_name"

    create_or_replace_path(detected_image_path)
    annotated_image.save(detected_image_path)

    formatted_det_data = format_label(det_data)


    with open(bbox_savepath, 'w') as json_file:
        json.dump(formatted_det_data, json_file, indent=4)

   

def sort_raw_image_key(filename):
    # Extract the digits from the filename and convert them to a tuple of integers
    base_name = os.path.basename(filename)
    digits = base_name.split('.')[0]  # Remove the file extension
    return tuple(map(int, digits.split('_')))

def batch_process_image(image_folder_path = "/data/home/jian/RLS_microwave/benchmark/control_panel_images", bbox_save_dir = "/data/home/jian/RLS_microwave/benchmark/control_panel_images_owl_bboxes", detected_image_dir = "/data/home/jian/RLS_microwave/benchmark/control_panel_images_owl_visualisation", validity_save_path = "/data/home/jian/RLS_microwave/benchmark/control_panel_images_validity", gpt_model_type = "gpt-4o"):

    machine_type_dirs = [os.path.join(image_folder_path, d) for d in os.listdir(image_folder_path) if os.path.isdir(os.path.join(image_folder_path, d))]
    for dir1 in machine_type_dirs:

        images_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, d)) and d.endswith(('.jpg', '.jpeg', '.png'))]
        images_dirs = sorted(images_dirs, key=sort_raw_image_key)
        
        
        relative_path = os.path.relpath(dir1, image_folder_path)
        save_bbox_dir = os.path.join(bbox_save_dir, relative_path) 
        save_img_dir = os.path.join(detected_image_dir, relative_path)
        #create_or_replace_path(save_bbox_dir)
        #create_or_replace_path(save_img_dir)

        for dir2 in images_dirs:
            
            #if "_2_bottle_washer/1_" not in dir2: # _1_dehumidifier/3_
            #    continue
            print("processing: ", dir2)
            if any(s in dir2 for s in ["_1_washing_machine/1_", "_2_rice_cooker/1_"]):
                continue 
            
            id_name = dir2.split("/")[-1].split(".")[0]
            
            # add it to a folder 
            machine_id = id_name.split("_")[0]
            pic_id = id_name.split("_")[1]
            save_bbox_machine_id_dir = os.path.join(save_bbox_dir, machine_id)
            
            save_img_machine_id_dir = os.path.join(save_img_dir, machine_id)
            save_bbox_path = os.path.join(save_bbox_machine_id_dir, pic_id + ".json")
            save_img_path = os.path.join(save_img_machine_id_dir, pic_id + ".png")
            process_image(dir2, save_bbox_path, save_img_path, dir1.split("/")[-1], machine_id, pic_id, validity_save_path, gpt_model_type, require_ocr=False)


def boxes_overlap(box1, box2):
    """
    Check if two bounding boxes overlap.
    Each box is defined by [x1, y1, x2, y2].
    """
    x1_min, y1_min, x1_max, y1_max = box1["bbox"]
    x2_min, y2_min, x2_max, y2_max = box2["bbox"]

    return not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)

def group_non_overlapping_boxes(objects):
    """
    Group bounding boxes into lists of non-overlapping boxes.
    """
    groups = []

    for bbox in objects:
        placed = False
        #bbox = object["bbox"]
        for group in groups:
            if all(not boxes_overlap(bbox, other_bbox) for other_bbox in group):
                group.append(bbox)
                placed = True
                break
        if not placed:
            groups.append([bbox])

    return groups

def boxes_within_distance(box1, box2, distance_threshold=0.1):
    """
    Check if two bounding boxes are within a specified distance.
    Each box is defined by [x1, y1, x2, y2] with normalized coordinates.
    """
    x1_min, y1_min, x1_max, y1_max = box1["bbox"]
    x2_min, y2_min, x2_max, y2_max = box2["bbox"]

    corners1 = [(x1_min, y1_min), (x1_min, y1_max), (x1_max, y1_min), (x1_max, y1_max)]
    corners2 = [(x2_min, y2_min), (x2_min, y2_max), (x2_max, y2_min), (x2_max, y2_max)]

    for (x1, y1) in corners1:
        for (x2, y2) in corners2:
            distance_x = abs(x1 - x2)
            distance_y = abs(y1 - y2)
            if distance_x <= distance_threshold and distance_y <= distance_threshold:
                return True

    return False

def group_boxes_within_distance(objects, distance_threshold=0.05):
    """
    Group bounding boxes into lists of boxes that are within a specified distance.
    """
    groups = []

    for bbox in objects:
        placed = False
        for group in groups:
            if all(not boxes_within_distance(bbox, other_bbox, distance_threshold) for other_bbox in group) and all(not boxes_overlap(bbox, other_bbox) for other_bbox in group):
                group.append(bbox)
                placed = True
                break
        if not placed:
            groups.append([bbox])

    return groups


def top_2_neighbors(query_bbox, bbox_list):
    """Find the top 2 neighboring bboxes to the query bbox."""
    def bbox_center(bbox):
        """Calculate the center of a bbox."""
        xmin, ymin, xmax, ymax = bbox
        return ((xmin + xmax) / 2, (ymin + ymax) / 2)

    def euclidean_distance(center1, center2):
        """Calculate the Euclidean distance between two points."""
        return math.sqrt((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2)
    
    query_center = bbox_center(query_bbox["bbox"])
    distances = []

    for bbox in bbox_list:
        if bbox["bbox"] != query_bbox["bbox"]:
            bbox_center_point = bbox_center(bbox["bbox"])
            distance = euclidean_distance(query_center, bbox_center_point)
            distances.append((distance, bbox))

    distances.sort(key=lambda x: x[0])
    top_2 = [distances[0][1], distances[1][1]] if len(distances) >= 2 else [distances[0][1]] if len(distances) == 1 else []

    return top_2
def make_query_images(image_path, bbox_savepath, query_image_root_dir):
    
    # load image 
    raw_image = Image.open(image_path)

    control_panel_bbox = crop_out_control_panel(raw_image)
    if not control_panel_bbox:
        return 
    
    data = []
    # load bboxes from json file
    with open(bbox_savepath, 'r') as json_file:
        data = json.load(json_file)
    
    for i, info in enumerate(data):
        annotated_image = copy.deepcopy(raw_image)

        # find closest two neighbouring bbox 
        # colour as blue 
        top_2= top_2_neighbors(info, data)
        

        query_image_save_path = os.path.join(query_image_root_dir, f"{i}_0.png")
        create_or_replace_path(query_image_save_path)
        #annotated_image.save(query_image_save_path)

        
        for j, neighbor_bbox in enumerate(top_2):
            
            annotated_image = visualize_image(annotated_image, bboxes = [neighbor_bbox["bbox"]] , return_img=True, labels=None , show=False, rect_color=bright_green, alpha=1)
        
        annotated_image = visualize_image(annotated_image, bboxes = [info["bbox"]] , return_img=True, labels=None , show=False, rect_color=bright_red,alpha=1)
        
        cropped_control_panel_image_annotated = crop_image_with_normalized_coords(annotated_image, control_panel_bbox)
        cropped_control_panel_image_clean = crop_image_with_normalized_coords(raw_image, control_panel_bbox)

        rescaled_info = convert_to_cropped_coords(control_panel_bbox, [info])[0]
        

        cropped_image,_ = crop_image_to_focus_on_bbox(cropped_control_panel_image_annotated, rescaled_info["bbox"], 5)
        cropped_image.save(query_image_save_path)

        blank_image_savepath = os.path.join(query_image_root_dir, f"{i}_1.png")
        create_or_replace_path(blank_image_savepath)
        blank_image,_ = crop_image_to_focus_on_bbox(cropped_control_panel_image_clean, rescaled_info["bbox"], 5)


        blank_image.save(blank_image_savepath)
        
    

def batch_make_query_images(image_dir, bbox_dir, query_image_root_dir):
    # list all directories in the image_dir
    machine_type_dirs = [os.path.join(image_dir, d) for d in os.listdir(image_dir) if os.path.isdir(os.path.join(image_dir, d))]
    # sort the directories
    machine_type_dirs.sort()
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        image_files = [os.path.join(dir1, d) for d in os.listdir(dir1) if d.endswith((".png", ".jpg", ".jpeg"))]
        
        machine_type = dir1.split("/")[-1] 
        if any(substring in machine_type for substring in ["_1_washing_machine", "_2_rice_cooker",]):
            continue
        # sort the image_files 
        
        image_files.sort()
        for image_file in image_files:
            machine_id = image_file.split("/")[-1].split(".")[0].split("_")[0]
            pic_id = image_file.split("/")[-1].split(".")[0].split("_")[1]
            bbox_save_path = os.path.join(bbox_dir, f"{machine_type}/{machine_id}/{pic_id}.json")
            query_image_dir = os.path.join(query_image_root_dir, f"{machine_type}/{machine_id}/{pic_id}")
            
            #if "_5_bread_maker/5" not in query_image_dir:
            #    continue
            #if not any(s in query_image_dir for s in ["_2_bottle_washer/1", "_2_bottle_washer/4", "_4_microwave_oven/2"]):
            #    continue 
            print("processing: ", image_file)
            make_query_images(image_file, bbox_save_path, query_image_dir)
            #exit()

if __name__ == "__main__":

     # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    # Detect Bounding Boxes from Photo
    # That contains control panel elements
    #
    ######################################
    gpt_model_type = "gpt-4o-2024-11-20"
    image_folder_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_2_control_panel_images/_1_selected')
    bbox_save_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_2_bboxes_on_control_panel')
    detected_image_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_3_bboxes_on_control_panel_visualisation')
    validity_save_path = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_1_validity_control_panel')

    #batch_process_image(image_folder_path, bbox_save_dir, detected_image_dir, validity_save_path, gpt_model_type)

    #process_image(image_path = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_0_raw/_1_microwave/2_0.jpeg'), bbox_savepath = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_2_bboxes/_1_microwave/2/0.json'), detected_image_path = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_3_bbox_visualisation/_1_microwave/2/0.png'))
    
    #######################################
    # Make Query Image for Entity Grounding 
    # For Each BBox, Draw its two neighbours
    #
    ######################################

    query_image_root_dir = os.path.expanduser(f'~/TextToActions/datasetv2/real_world/_2_control_panel_images/_2_ground_control_panel_elements/{gpt_model_type}/_4_query_images_bbox_to_name')

    batch_make_query_images(image_folder_path, bbox_save_dir, query_image_root_dir)

    #make_query_images(image_path = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_0_raw/_2_washing_machine/3_0.jpeg'), bbox_savepath = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_3_bboxes_on_control_panel/_2_washing_machine/3/0.json'), query_image_root_dir = os.path.expanduser('~/TextToActions/dataset/_2_control_panel_images/_5_query_images_bbox_to_name/_2_washing_machine/3/0'))
    









    







    
