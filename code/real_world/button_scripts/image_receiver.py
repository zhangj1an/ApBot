# haobot_policy_api.py


# srun -u -o "api-haobotperception-log.out" -w crane6 --mem=20000 --gres=gpu:1 --cpus-per-task=4 --time=03:00:00 --job-name "haobotreceiver" uvicorn image_receiver:haobotpolicy --host=0.0.0.0 --port=4011 --reload --loop asyncio


import base64
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PIL import Image
from io import BytesIO
import uvicorn
from datetime import datetime
import os
import os 
import sys
import shutil
import json
import time 
sys.path.append(os.path.expanduser("~/TextToActions/code/"))
sys.path.append(os.path.expanduser("~/TextToActions/code/real_world/button_scripts/tools"))
from real_world.button_scripts.generate_open_loop_policy import ground_open_loop_policy, prepare_directories_offline
# Initialize the app
haobotpolicy = FastAPI()

# Define input payload
class ImagePayload(BaseModel):
    rgb: str  # Base64 encoded image string

@haobotpolicy.post("/haobot_policy_predict/")
async def haobot_policy_predict(image_payload: ImagePayload):
    # Load image from base64
    """
    filepath = os.path.expanduser("~/TextToActions/code/real_world/button_scripts/induction_cooker_task_coords_20250428_204916.json")
    # load json as list 
    with open(filepath, "r") as f:
        data = json.load(f)
    return data
    """
    try:
        image_data = base64.b64decode(image_payload.rgb)
        image = Image.open(BytesIO(image_data)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image data: {e}")

    # Generate filename based on current time
    now = datetime.now()
    timestring = now.strftime("%Y%m%d_%H%M%S") 
    filename = now.strftime("%Y%m%d_%H%M%S") + ".png"  # e.g., 20250427_210530.png

    # Save the image to current folder
    appliance_type =  "water_dispenser" #"water_dispenser", "induction_cooker", "blender"
    method_name = "ours_oracle_model"
    parameter_dict = prepare_directories_offline(appliance_type, method_name, timestring)
    open_loop_coords = ground_open_loop_policy(appliance_type, image, parameter_dict, timestring)

    with open(f"{appliance_type}_task_coords.json", "w") as f:
        json.dump(open_loop_coords, f, indent=4)

    #filepath = os.path.expanduser("~/TextToActions/code/real_world/button_scripts/data/blender/_0_input/0.png")
    # Save to first location
    image.save(f"./temp_input/{appliance_type}_{filename}")

    # Save to second location
    save_path = parameter_dict["control_panel_image_filepath"]
    print(f"Trying to save image to {save_path}... ")
    image.save(save_path)

    return open_loop_coords

if __name__ == "__main__":
    uvicorn.run(haobotpolicy, host="0.0.0.0", port=4011)
