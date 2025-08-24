import os
import sys
import json
sys.path.append(os.path.expanduser("~/TextToActions/code"))

from PIL import Image, ImageDraw, ImageFont

from PIL import Image
from io import BytesIO
from skimage import io as skimage_io
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import requests
import io
import random
plt.switch_backend('Agg')

def visualize_image(image, masks=None, bboxes=None, points=None, show=True, return_img=False, labels=None, rect_color="blue", text_color="red", alpha=1, font_size = 5, position = "right"):
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

            if position == "right":
                label_y = y2 + 10 if y2 + 10 < img_height else img_height
                label_x = x2 + 10 if x2 + 10 < img_width else img_width
                plt.gca().text(label_x, label_y, label, color='white', size=font_size, 
                           bbox=dict(facecolor=text_color, alpha=alpha, edgecolor='none', boxstyle='round,pad=0.3'))
            elif position == "center":
                label_y = y1 + height/2
                label_x = x1 + width/2

                plt.gca().text(label_x, label_y, label, color='white', size=font_size, 
               ha='center', va='center',  # Align text properly
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


def visualize_bboxes_with_legend(image_path, annotation_info, output_image_savepath, output_label_savepath, setting):
    """
    Draws all bounding boxes on a single image and adds a legend linking each bbox index to its action name.
    """
    # Load image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    print("output_image_savepath:", output_image_savepath)
    #image.save(output_image_savepath.replace("label.jpg", "original.jpg"))
    # Assign indices to unique bounding boxes
    bbox_to_index = {}
    legend = []
    index = 1
    index_to_bbox = {}
    for item in annotation_info:
        bbox_tuple = tuple(item['bbox'])
        if bbox_tuple not in bbox_to_index:
            bbox_to_index[bbox_tuple] = index
            index += 1
        legend.append((bbox_to_index[bbox_tuple], item['label']))
        index_to_bbox[bbox_to_index[bbox_tuple]] = bbox_tuple
    
    # save the control element name to json files with indent 4 
    if setting == "no_label" and output_label_savepath != "":
        with open(output_label_savepath, "w") as f:
            json.dump(index_to_bbox, f, indent=4)
        print(f"saved mapping from bbox index to bbox coord at {output_image_savepath}")
        
    # Convert normalized bbox coordinates to image scale and annotate
    if setting == "with_label":
        annotated_image = visualize_image(
            image, 
            bboxes=[list(bbox) for bbox in bbox_to_index.keys()],
            labels=[str(bbox_to_index[bbox]) for bbox in bbox_to_index.keys()],
            show=False, 
            return_img=True, 
            rect_color="blue", 
            text_color="blue",
            position = "right",
        )
    elif setting == "no_label":
        annotated_image = visualize_image(
            image, 
            bboxes=[list(bbox) for bbox in bbox_to_index.keys()],
            labels=[str(bbox_to_index[bbox]) for bbox in bbox_to_index.keys()],
            show=False, 
            return_img=True, 
            rect_color="green", 
            text_color="green",
            alpha = 1,
            font_size = 5,
            position = "center"
        )
        """
        visualize_image(image, masks=None, bboxes=None, points=None, show=True, return_img=False, labels=None, rect_color="blue", text_color="red", alpha=1, font_size = 5)
        """
    # Load a font with a size similar to matplotlib's font_size=5
    if setting == "no_label":
        font_size = 20
    elif setting == "with_label": 
        font_size = 40
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # Fallback if DejaVuSans is unavailable

    if setting == "with_label":
        # Measure the longest legend text width
        legend_texts = [f"{idx}: {label}" for idx, label in sorted(set(legend))]
        longest_text = max(legend_texts, key=lambda t: font.getbbox(t)[2] - font.getbbox(t)[0])
        legend_width = font.getbbox(longest_text)[2] - font.getbbox(longest_text)[0] + 10  # Add padding

        # Define the width of the right section
        extra_width = max(legend_width + 20, 150)  # Ensure minimum space
        legend_x_offset = annotated_image.width + 10  # Starting x position

        # Calculate legend height
        text_heights = [font.getbbox(text)[3] - font.getbbox(text)[1] for text in legend_texts]
        legend_height = sum(text_heights) + 5 * len(legend_texts)  # Add padding between lines

        # Create new image with space for the legend on the right
        new_image = Image.new("RGB", (annotated_image.width + extra_width, annotated_image.height), "white")
        new_image.paste(annotated_image, (0, 0))
        draw = ImageDraw.Draw(new_image)

         # Compute the starting Y position for the legend (aligned to bottom of the right section)
        legend_y_offset = annotated_image.height - legend_height - 10  # Leave some bottom padding
        for text in legend_texts:
            bbox = font.getbbox(text)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            draw.text((legend_x_offset, legend_y_offset), text, fill="black", font=font)  # Left align
            legend_y_offset += text_height + 5  # Adjust spacing based on font height
            # Save output
        new_image.save(output_image_savepath)
        print(f"Saved visualization at {output_image_savepath}")
    elif setting == "no_label":
        new_image = Image.new("RGB", (annotated_image.width, annotated_image.height), "white")
        new_image.paste(annotated_image, (0, 0))
        draw = ImageDraw.Draw(new_image)
        new_image.save(output_image_savepath)
        print(f"Saved visualization at {output_image_savepath}")

        # create the labels as json files, match each element name to an index. 

if __name__ == "__main__":

    ## visualise control panel element

    def visualise_single_control_panel_element():
        image_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected/_1_microwave/4_0.jpeg")
        image = Image.open(image_filepath)
        grounded_element_bboxes_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_0_control_panel_element_bbox/_3_proposed_control_panel_element_bbox/_1_microwave/4.json")
        output_image_savepath = "./dial.png"
        with open(grounded_element_bboxes_filepath, "r") as f:
            proposed_entities = json.load(f)
        annotation_info = []
        for proposed_entity in proposed_entities:
            bboxes = proposed_entity["grounded_bboxes"]
            element_name = proposed_entity["element_name"]
            if element_name == "power_button":
                for item in bboxes:
                    if item["image_name"] == "4_0":
                        bbox = item["bbox"]
                        labelled_image = visualize_image(image, bboxes = [bbox], return_img=True, text_color = "blue", labels = [element_name],rect_color = "blue", font_size = 5, position = "right")
                        labelled_image.save(output_image_savepath)
    def visualise_single_action():
        image_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_2_control_panel_images/_1_selected/_1_microwave/4_0.jpeg")
        image = Image.open(image_filepath)
        grounded_element_bboxes_filepath = os.path.expanduser("~/TextToActions/dataset/simulated/_4_visual_grounding/gpt-4o-2024-11-20/_1_action_names/_2_proposed_world_model_action_bbox/_1_microwave/4.json")
        output_image_savepath = "./dial.png"
        with open(grounded_element_bboxes_filepath, "r") as f:
            proposed_entities = json.load(f)
        annotation_info = []
        for proposed_entity in proposed_entities:
            bboxes = proposed_entity["bboxes"]
            action_name = proposed_entity["action"]
            if action_name == "press_power_button":
                for item in bboxes:
                    if item["image_name"] == "4_0":
                        bbox = item["bbox"]
                        labelled_image = visualize_image(image, bboxes = bbox, return_img=True, text_color = "blue", labels = [action_name],rect_color = "blue", font_size = 5, position = "right")
                        labelled_image.save(output_image_savepath)
    def visualise_all_bboxes():
        pass 
    
    
    

    

    

