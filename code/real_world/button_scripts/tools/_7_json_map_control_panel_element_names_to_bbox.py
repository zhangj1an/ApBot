import json
import os 
import os 
import _0_t2a_config
from utils.create_or_replace_path import create_or_replace_path


def batch_map_element_to_bboxes(index_mapping_root_dir, located_bboxes_root_dir, output_root_dir):
    # list all machine types dir 
    index_mapping_machine_type_dir = os.listdir(index_mapping_root_dir)
    for machine_type_dir in index_mapping_machine_type_dir:
        # list all machine id file that ends with .json
        index_mapping_machine_id_files = [f for f in os.listdir(os.path.join(index_mapping_root_dir, machine_type_dir)) if f.endswith(".json")]
        for index_mapping_machine_id_file in index_mapping_machine_id_files:
            
            machine_id = index_mapping_machine_id_file.split(".")[0]
            located_bboxes_dir = os.path.join(located_bboxes_root_dir, machine_type_dir, machine_id)
            output_filepath = os.path.join(output_root_dir, machine_type_dir, machine_id + ".json")
            index_mapping_filepath = os.path.join(index_mapping_root_dir, machine_type_dir, index_mapping_machine_id_file)
            
            map_element_to_bboxes(index_mapping_filepath, located_bboxes_dir, output_filepath)
    pass

def map_element_to_bboxes(index_mapping_filepath, located_bboxes_dir, output_filepath):
    # load json from index_mapping_filepath as a list 
    with open(index_mapping_filepath, "r") as f:
        index_mapping = json.load(f)
    # load json from located_bboxes_dir as a list
    machine_id = index_mapping_filepath.split("/")[-1].split(".")[0]
    machine_type = index_mapping_filepath.split("/")[-2]
    # if located_bboxes_dir is a file, then it is a single file
    if os.path.isfile(located_bboxes_dir):
        located_bboxes_files = [located_bboxes_dir]
    elif os.path.isdir(located_bboxes_dir):
        located_bboxes_files = [f for f in os.listdir(located_bboxes_dir) if f.endswith(".json")]
    # for each element in index_mapping, find the corresponding bboxes in located_bboxes
    print("processing ", index_mapping_filepath)
    for element in index_mapping:
        element_name = element["element_name"]
        element["grounded_bboxes"] =  []
        indexed_bboxes = element["bboxes"]
        for indexed_bbox in indexed_bboxes:
            image_name = indexed_bbox["image_name"]
            if len(image_name.split("_")) == 2:
                image_id = image_name.split("_")[1]
            else:
                image_id = image_name
            for located_bbox_file in located_bboxes_files:
                
                located_bbox_file_id = located_bbox_file.split(".")[0]
                # if located_bbox_file_id is not a number:
                if str(image_id) == str(located_bbox_file_id) or not located_bbox_file_id.isdigit():
                    located_bboxes_filepath = os.path.join(located_bboxes_dir, located_bbox_file)
                    with open(located_bboxes_filepath, "r") as f:
                        located_bboxes = json.load(f)
                    if len(indexed_bbox["bbox_id"]) < 1:
                        continue
                    indexed_bbox_id = indexed_bbox["bbox_id"][0]
                    for bbox in located_bboxes:

                        if str(bbox["id"]) == str(indexed_bbox_id):
                            element["grounded_bboxes"].append({
                                "image_name": image_name,
                                "bbox": bbox["bbox"]
                            })
    create_or_replace_path(output_filepath) 
    # save index mapping to output directory 
    with open(output_filepath, "w") as f:
        json.dump(index_mapping, f, indent=4)
    """
    {
        "element_name": "max_crisp_button",
        "bboxes": [
            {"image_name": "0_2", "bbox_id": [26]},
            {"image_name": "0_1", "bbox_id": [5]},
            {"image_name": "0_0", "bbox_id": [44]}
        ]
    },
    """
    """ located bboxes: a list of below in each file json
    {
        "score": 0.9998470712714901,
        "bbox": [
            0.4852941176470588,
            0.30514705882352944,
            0.545751633986928,
            0.3235294117647059
        ],
        "box_name": "MAX",
        "id": 0
    },
    """

    """
    {"action": "press_max_crisp_button", "bbox_label": "max_crisp_button", "action_type": "press_button", "bboxes": [{"image_name": "0_1", "bbox": [0.2679738562091503, 0.32965686274509803, 0.37336601307189543, 0.36519607843137253]}, {"image_name": "0_2", "bbox": [0.27941176470588236, 0.40012254901960786, 0.39950980392156865, 0.43566176470588236]}, {"image_name": "0_0", "bbox": [0.30637254901960786, 0.38848039215686275, 0.4084967320261438, 0.4258578431372549]}]}
    """
    # map element name to bboxes
    pass

if __name__ == "__main__":

    # srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Map Entity to BBox coordinate for all appliances
    #
    #######################################

    index_mapping_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_2_control_panel_element_index_json_unique')
    located_bboxes_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_2_control_panel_images/_3_bboxes_on_control_panel')
    output_root_dir = os.path.expanduser('~/TextToActions/dataset/simulated/_4_visual_grounding/_3_proposed_control_panel_element_bbox')

    # below line deletes all backup files
    # find . -type f -name "*_backup.json" -exec rm {} +
    #batch_map_element_to_bboxes(index_mapping_root_dir, located_bboxes_root_dir, output_root_dir)

    #######################################
    #
    # Map Entity to BBox coordinate for one appliance
    #
    #######################################

    machine_type = "_2_washing_machine"
    machine_id = "3"
    index_mapping_filepath = os.path.expanduser(f'~/TextToActions/dataset/simulated/_4_visual_grounding/_2_control_panel_element_index_json_unique/{machine_type}/{machine_id}.json')
    located_bboxes_dir = os.path.expanduser(f'~/TextToActions/dataset/simulated/_2_control_panel_images/_3_bboxes_on_control_panel/{machine_type}/{machine_id}')
    output_filepath = os.path.expanduser(f'~/TextToActions/dataset/simulated/_4_visual_grounding/_3_proposed_control_panel_element_bbox/{machine_type}/{machine_id}.json')

    #map_element_to_bboxes(index_mapping_filepath, located_bboxes_dir, output_filepath)