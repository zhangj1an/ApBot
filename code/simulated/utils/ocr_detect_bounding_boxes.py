import easyocr 
import cv2
import torch    
def ocr_detect_bounding_boxes(image_path):
    # Initialize the EasyOCR reader
    print("CUDA available:", torch.cuda.is_available())
    reader = easyocr.Reader(['en'])  # Specify languages as needed

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Perform OCR using EasyOCR
    # default
    results = reader.readtext(image, text_threshold=0.5, low_text = 0.2, min_size = 5, link_threshold = 0.4, contrast_ths = 0.05, adjust_contrast = 1.0, paragraph = False)
    

    # Initialize a list to hold the bounding box data
    boxes = []

    # Loop through the detected text and bounding boxes
    
    for result in results:
        #print(result)
        bbox, text, score = result
        #bbox, text = result
        x_min = min(bbox, key=lambda x: x[0])[0]
        y_min = min(bbox, key=lambda x: x[1])[1]
        x_max = max(bbox, key=lambda x: x[0])[0]
        y_max = max(bbox, key=lambda x: x[1])[1]
        box = {
            "score": score,
            "bbox": [
                x_min / image.shape[1], y_min / image.shape[0],
                x_max / image.shape[1], y_max / image.shape[0]
            ],
            "label": text
        }
        boxes.append(box)
    
    return boxes
