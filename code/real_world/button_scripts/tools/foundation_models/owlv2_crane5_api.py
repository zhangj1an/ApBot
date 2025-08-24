# Existing imports

# bash command
# srun -u -o "api-owlv2-log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=4 --time=03:00:00 --job-name "owlv2" uvicorn owlv2_crane5_api:app --host=0.0.0.0 --port=4229 --reload --loop asyncio

import sys
#sys.path.append(os.path.expanduser("~/TextToActions/code"))

from transformers.utils.constants import OPENAI_CLIP_MEAN, OPENAI_CLIP_STD
import os
from PIL import Image
import jax
import cv2
from matplotlib import pyplot as plt
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from scipy.special import expit as sigmoid
from skimage import io as skimage_io
import uvicorn
import base64
from io import BytesIO
import torch
from transformers import AutoTokenizer, AutoModel, BitsAndBytesConfig, AutoProcessor, Owlv2ForObjectDetection

print(f"Current Conda environment path: {sys.prefix}", flush=True)
#from internvl_8b import  build_transform, dynamic_preprocess


# InternVL2-8B specific imports
from torchvision.transforms import ToTensor

# Load OWL-ViT model and processor
processor = AutoProcessor.from_pretrained("google/owlv2-large-patch14-ensemble")
owl_model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-large-patch14-ensemble").to("cuda")

# Load InternVL2-8B model and tokenizer

app = FastAPI()


def get_preprocessed_image(pixel_values):
    pixel_values = pixel_values.squeeze().numpy()
    unnormalized_image = (pixel_values * np.array(OPENAI_CLIP_STD)[:, None, None]) + np.array(OPENAI_CLIP_MEAN)[:, None, None]
    unnormalized_image = (unnormalized_image * 255).astype(np.uint8)
    unnormalized_image = np.moveaxis(unnormalized_image, 0, -1)
    unnormalized_image = Image.fromarray(unnormalized_image)
    return unnormalized_image

class Payload(BaseModel):
    payload: str

class QueryImagePayload(BaseModel):
    image: str
    query_image: str
    bbox_conf_threshold: float = 0.2
    bbox_score_top_k: int = 20
    output_path: str = "output_query_image.png"

class ImageQueryPayload(BaseModel):
    text_queries: List[str]
    image: str
    bbox_conf_threshold: float = 0.9
    bbox_score_top_k: int = 20
    output_path: str = "output.png"

class InternVLQueryPayload(BaseModel):
    question: str
    image: str

@app.post("/test/")
async def test(payload: Payload):
    return {"received_payload": payload.payload}

@app.post("/owlv2_predict/")
async def owlv2_predict(image_query_payload: ImageQueryPayload):
    text_queries = image_query_payload.text_queries
    image = image_query_payload.image
    bbox_conf_threshold = image_query_payload.bbox_conf_threshold
    bbox_score_top_k = image_query_payload.bbox_score_top_k
    output_path = image_query_payload.output_path
    
    # Load image
    try:
        image_data = base64.b64decode(image)
        image = Image.open(BytesIO(image_data)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image data: {e}")

    inputs = processor(
        text=[text_queries],  # 2D list needed
        images=image, 
        return_tensors="pt"
    ).to("cuda")

    # Forward model
    with torch.no_grad():
        outputs = owl_model(**inputs)
        
    padded_image_size = inputs.pixel_values.shape[2:]  # (batch, channel, w?, h?)
    target_sizes=torch.Tensor([padded_image_size]).cuda()  # 2D list needed
    results = processor.post_process_object_detection(
        outputs=outputs, 
        target_sizes=target_sizes,
        threshold=bbox_conf_threshold
    )

    results = results[0]  # Retrieve predictions for the first image for the corresponding text queries
    
    bboxes, scores, labels = results["boxes"], results["scores"], results["labels"]

    # Restore bbox names
    box_names = [text_queries[i] for i in labels]
    padded_width, padded_height = padded_image_size
    width, height = image.size
    longest_edge = max(width, height)
    scale_ratio = longest_edge / padded_width
    for bbox in bboxes:
        bbox[0::2] = bbox[0::2] * scale_ratio / width
        bbox[1::2] = bbox[1::2] * scale_ratio / height

    bboxes = bboxes.tolist()
    scores = scores.tolist()

    return {"status": "success",  'scores': scores, 'bboxes': bboxes, 'box_names': box_names}

@app.post("/owlv2_predict_query_image/")
async def owlv2_predict_query_image(query_image_payload: QueryImagePayload):
    image = query_image_payload.image
    query_image = query_image_payload.query_image
    bbox_conf_threshold = query_image_payload.bbox_conf_threshold
    output_path = query_image_payload.output_path
    bbox_score_top_k = query_image_payload.bbox_score_top_k

    # Load image and query image
    try:
        image_data = base64.b64decode(image)
        query_image_data = base64.b64decode(query_image)
        image = Image.open(BytesIO(image_data)).convert("RGB")
        query_image = Image.open(BytesIO(query_image_data)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image or query image data: {e}")

    # Process target image
    target_pixel_values = processor(images=image, return_tensors="pt").pixel_values
    unnormalized_target_image = get_preprocessed_image(target_pixel_values)
    inputs = processor(
        images=image, 
        query_images=query_image, 
        return_tensors="pt"
    ).to("cuda")

    # Forward model
    with torch.no_grad():
        outputs = owl_model.image_guided_detection(**inputs)

    img = cv2.cvtColor(np.array(unnormalized_target_image), cv2.COLOR_BGR2RGB)
    outputs.logits = outputs.logits.cpu()
    outputs.target_pred_boxes = outputs.target_pred_boxes.cpu()

    padded_image_size = inputs.pixel_values.shape[2:] 
    target_sizes = torch.Tensor([unnormalized_target_image.size[::-1]])
    # good values are 0.98, 0.95
    results = processor.post_process_image_guided_detection(outputs=outputs, threshold=bbox_conf_threshold, nms_threshold=0.3, target_sizes=target_sizes)

    results = results[0]  # Retrieve predictions for the first image and query image
    
    bboxes, scores, labels = results["boxes"], results["scores"], results["labels"]


    width, height = image.size
    longest_edge = max(width, height)
    padded_width, padded_height = padded_image_size
    scale_ratio = longest_edge / padded_width
    for bbox in bboxes:
        bbox[0::2] = bbox[0::2] * scale_ratio / width
        bbox[1::2] = bbox[1::2] * scale_ratio / height
    bboxes = bboxes.tolist()
    scores = scores.tolist()

    return {"status": "success", 'scores': scores, 'bboxes': bboxes}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4229)
