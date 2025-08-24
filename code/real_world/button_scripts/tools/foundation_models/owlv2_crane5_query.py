# bash command 
# srun -u -o "log.out" -w crane3 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “pipeline” python3 owlv2_crane5_query.py
# srun -u -o "log.out" --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “pipeline” python3 owlv2_crane5_query.py

import base64
import requests
import json
from PIL import Image
from io import BytesIO
from skimage import io as skimage_io
from skimage import transform as skimage_transform
from skimage import data as skimage_data
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from typing import List as list
import requests
import io
import random
plt.switch_backend('Agg')

import base64
from typing import List as list
import os

def convert_pil_image_to_base64(image: Image.Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def visualize_image(image, masks=None, bboxes=None, points=None, show=True, return_img=False, labels=None, rect_color="blue", text_color="red", alpha=1):
    img_height, img_width = np.array(image).shape[:2]
    plt.tight_layout()
    plt.imshow(image, aspect='equal')
    plt.axis('off')
    plot = plt.gcf()

    # Overlay mask if provided
    if masks is not None:
        for mask in masks:
            colored_mask = np.zeros((*mask.shape, 4))
            random_color = [0.5 + 0.5 * random.random() for _ in range(3)] + [0.8]  # RGBA format
            colored_mask[mask > 0] = random_color
    
    # Draw bounding boxes if provided
    if bboxes is not None and labels is not None:
        for bbox, label in zip(bboxes, labels):
            x1, y1, x2, y2 = bbox
            x1 *= img_width
            y1 *= img_height
            x2 *= img_width
            y2 *= img_height
            
            width = x2 - x1
            height = y2 - y1
            rect = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor=rect_color, facecolor='none')
            plt.gca().add_patch(rect)

            label_y = y2 + 10 if y2 + 10 < img_height else img_height
            label_x = x2 + 10 if x2 + 10 < img_width else img_width

            plt.gca().text(label_x, label_y, label, color='white', size=5, 
                           bbox=dict(facecolor=text_color, alpha=alpha, edgecolor='none', boxstyle='round,pad=0.3'))
    
    if bboxes is not None and labels is None:
        print("visualising bbox without labels:", bboxes)
        for bbox in bboxes:
            x1, y1, x2, y2 = bbox
            x1 *= img_width
            y1 *= img_height
            x2 *= img_width
            y2 *= img_height
            
            width = x2 - x1
            height = y2 - y1
            rect = patches.Rectangle((x1, y1), width, height, linewidth=1, edgecolor=rect_color, facecolor='none')
            plt.gca().add_patch(rect)

            
    if points is not None:
        points = np.array(points)
        points[:, 0] = points[:, 0] * img_width
        points[:, 1] = points[:, 1] * img_height
        plt.scatter(points[:, 0], points[:, 1], c='red', s=50)
        plt.scatter(points[:, 0], points[:, 1], c='yellow', s=30)

    if return_img:
        buffer = io.BytesIO()
        plot.savefig(buffer, format='png', dpi=500, bbox_inches='tight', pad_inches=0)
        buffer.seek(0)
        img = Image.open(buffer)

    if show:
        pass

    plt.close(plot)

    if return_img:
        return img
    else:
        return None

def bbox_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1b, y1b, x2b, y2b = box2

    x_left = max(x1, x1b)
    y_top = max(y1, y1b)
    x_right = min(x2, x2b)
    y_bottom = min(y2, y2b)

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection_area = (x_right - x_left) * (y_bottom - y_top)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2b - x1b) * (y2b - y1b)
    union_area = box1_area + box2_area - intersection_area

    iou = intersection_area / union_area
    return iou

def filter_bboxes(det_data, threshold=0.95):
    def bbox_area(bbox):
        x_min, y_min, x_max, y_max = bbox
        return (x_max - x_min) * (y_max - y_min)

    def is_bbox_inside(inner, outer):
        ix_min, iy_min, ix_max, iy_max = inner
        ox_min, oy_min, ox_max, oy_max = outer
        return ix_min >= ox_min and iy_min >= oy_min and ix_max <= ox_max and iy_max <= oy_max

    # Step 1: Existing filtering by IoU
    filtered_data = []
    det_data = sorted(det_data, key=lambda x: x['score'], reverse=True)
    while det_data:
        base = det_data.pop(0)
        filtered_data.append(base)
        det_data = [item for item in det_data if bbox_iou(base['bbox'], item['bbox']) <= threshold]

    # Step 2: New filtering - remove fully covered small boxes
    final_data = []
    for i, box_i in enumerate(filtered_data):
        keep = True
        for j, box_j in enumerate(filtered_data):
            if i == j:
                continue
            # If box_i is smaller and fully inside box_j, remove it
            if bbox_area(box_i['bbox']) < bbox_area(box_j['bbox']) and is_bbox_inside(box_i['bbox'], box_j['bbox']):
                keep = False
                break
        if keep:
            final_data.append(box_i)

    return final_data


def convert_float32_to_float(data):
    if isinstance(data, list):
        return [convert_float32_to_float(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_float32_to_float(value) for key, value in data.items()}
    elif isinstance(data, np.float32):
        return float(data)
    else:
        return data

def format_label(det_data):
    det_data = convert_float32_to_float(det_data)
    id = 0
    for item in det_data:
        item['id'] = id
        id += 1
    return det_data

class OWLViT:

    def __init__(self, server_url="http://crane6.d2.comp.nus.edu.sg:4229"):
        self.server_url = server_url
        print("Server URL:", self.server_url)

    def sending_test(self, text):
        payload = {"payload": text}
        response = requests.post(self.server_url + "/test/", json=payload)
        if response.status_code != 200:
            raise ConnectionError(f"Request failed with status code {response.status_code}")
        return response

    def detect_objects(self, image: Image.Image, text_queries: list[str], bbox_score_top_k=20, bbox_conf_threshold=0.5, output_path="output.png"):
        base64_image = convert_pil_image_to_base64(image.convert('RGB'))
        payload = {
            "text_queries": text_queries,
            "image": base64_image,
            "bbox_score_top_k": bbox_score_top_k,
            "bbox_conf_threshold": bbox_conf_threshold,
            "output_path": output_path
        }
        response = requests.post(self.server_url + "/owlv2_predict/", json=payload)
        if response.status_code != 200:
            raise ConnectionError(f"Request failed with status code {response.status_code}")

        resp_data = json.loads(response.text)
        scores = resp_data['scores']
        bboxes = resp_data['bboxes']
        labels = resp_data['box_names']

        assert len(scores) == len(bboxes), "Server returned data with different lengths. Something is wrong, most probably on the server side."

        dict_data = [{'score': score, 'bbox': bbox, 'label': label} for score, bbox, label in zip(scores, bboxes, labels)]
        return dict_data

    def detect_query_image(self, image: Image.Image, query_image: Image.Image, bbox_conf_threshold=0.5, output_path="output_query_image.png"):
        base64_image = convert_pil_image_to_base64(image.convert('RGB'))
        base64_query_image = convert_pil_image_to_base64(query_image.convert('RGB'))
        
        payload = {
            "image": base64_image,
            "query_image": base64_query_image,
            "bbox_conf_threshold": bbox_conf_threshold,
            "output_path": output_path
        }
        
        response = requests.post(self.server_url + "/owlv2_predict_query_image/", json=payload)
        if response.status_code != 200:
            raise ConnectionError(f"Request failed with status code {response.status_code}")

        resp_data = json.loads(response.text)
        scores = resp_data['scores']
        bboxes = resp_data['bboxes']

        assert len(scores) == len(bboxes), "Server returned data with different lengths. Something is wrong, most probably on the server side."

        dict_data = [{'score': score, 'bbox': bbox} for score, bbox in zip(scores, bboxes)]
        return dict_data
    
class InternVL:

    def __init__(self, server_url="http://crane6.d2.comp.nus.edu.sg:4229"):
        self.server_url = server_url

    def query_image(self, image: Image.Image, question: str):
        base64_image = convert_pil_image_to_base64(image.convert('RGB'))
        payload = {
            "question": question,
            "image": base64_image
        }
        response = requests.post(self.server_url + "/internvl_predict/", json=payload)
        if response.status_code != 200:
            raise ConnectionError(f"Request failed with status code {response.status_code}")

        resp_data = json.loads(response.text)
        return resp_data['response']

if __name__ == "__main__":
    from PIL import Image

    # Initialize the detectors with the server URL
    owl_detector = OWLViT(server_url="http://crane6.d2.comp.nus.edu.sg:4229")
    internvl_detector = InternVL(server_url="http://crane6.d2.comp.nus.edu.sg:4229")

    # Load an image
    image_path = "/data/home/jian/RLS_microwave/benchmark_3/_2_control_panel_images/_0_raw/_2_washing_machine/0_0.jpeg"
    image = Image.open(image_path)

    """
    # Define text queries for OWLViT
    text_queries = ["button", "dial"]
    
    # Detect objects in the image using OWLViT
    results = owl_detector.detect_objects(image, text_queries, bbox_conf_threshold=0.1)
    print(results)
    
    # Visualize and save the results
    image_with_bboxes = visualize_image(image, bboxes=[obj["bbox"] for obj in results], return_img=True, labels=[obj["label"] for obj in results])
    image_with_bboxes.save("output_owlvit.png")
    """
    # Define a question for InternVL
    question = "Please describe the image shortly."

    # Query the image using InternVL
    response = internvl_detector.query_image(image, question)
    print(f'User: {question}\nAssistant: {response}')
