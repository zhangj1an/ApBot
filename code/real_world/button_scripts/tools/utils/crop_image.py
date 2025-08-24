
from PIL import Image
import copy
def crop_image_to_focus_on_bbox(image, bbox, distance_threshold):
    """
    Crop an image to include only the area within a specified distance threshold from a bounding box center.
    
    :param image: Input image
    :param bbox: Bounding box in the format (xmin, ymin, xmax, ymax)
    :param distance_threshold: Distance threshold as a multiple of the bounding box width
    :return: Cropped image
    """
    width, height = image.size
    xmin, ymin, xmax, ymax = bbox
    x = xmin * width
    y = ymin * height
    w = (xmax - xmin) * width
    h = (ymax - ymin) * height

    bbox_center_x = x + w / 2
    bbox_center_y = y + h / 2
    crop_width = w * distance_threshold
    crop_height = h * distance_threshold

    left = bbox_center_x - crop_width
    upper = bbox_center_y - crop_height
    right = bbox_center_x + crop_width
    lower = bbox_center_y + crop_height

    # Adjust if the cropping box goes out of image bounds
    if left < 0:
        right += abs(left)
        left = 0
    if upper < 0:
        lower += abs(upper)
        upper = 0
    if right > image.width:
        left -= (right - image.width)
        right = image.width
    if lower > image.height:
        upper -= (lower - image.height)
        lower = image.height

    # Ensure the adjusted values are within bounds
    left = max(left, 0)
    upper = max(upper, 0)
    right = min(right, image.width)
    lower = min(lower, image.height)

    cropped_image = image.crop((left, upper, right, lower))

    # Convert crop coordinates to normalized format
    xmin_crop = left / width
    ymin_crop = upper / height
    xmax_crop = right / width
    ymax_crop = lower / height
    cropped_coord = [xmin_crop, ymin_crop, xmax_crop, ymax_crop]
    return cropped_image, cropped_coord


def convert_to_original_coords(crop_coord, source_objects):
    detected_objects = copy.deepcopy(source_objects)
    xmin_crop, ymin_crop, xmax_crop, ymax_crop = crop_coord
    crop_width = xmax_crop - xmin_crop
    crop_height = ymax_crop - ymin_crop

    original_coords_list = []

    for detected_object in detected_objects:
        #print("detected_object: ", detected_object)
        xmin_obj, ymin_obj, xmax_obj, ymax_obj = detected_object["bbox"]
        
        xmin_original = xmin_obj * crop_width + xmin_crop
        ymin_original = ymin_obj * crop_height + ymin_crop
        xmax_original = xmax_obj * crop_width + xmin_crop
        ymax_original = ymax_obj * crop_height + ymin_crop

        detected_object["bbox"] = [xmin_original, ymin_original, xmax_original, ymax_original]
        original_coords_list.append(detected_object)
    
    return original_coords_list