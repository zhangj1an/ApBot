
import warnings
warnings.filterwarnings("ignore")

import os
import fitz # imports the pymupdf library
import pypdfium2 as pdfium
import re 
import _0_t2a_config
from foundation_models.gpt_4o_model import GPT4O
import shutil
from PIL import Image
from pdf2image import convert_from_path
import tempfile
import threading
Image.MAX_IMAGE_PIXELS = 300_000_000 
file_lock = threading.Lock()

#####################################
#
#
# Method: Traditional OCR
#
#
#####################################

def pdf_to_path(pdf_file_path, txt_file_path):
    print(pdf_file_path)
    doc = fitz.open(pdf_file_path) # open a document
    text_file = open(txt_file_path, "w")
    for page in doc: # iterate the document pages
        #print(f"page {page}")
        text = page.get_text() # get plain text encoded as UTF-8
        text_file.write(text)
    print(f"generated text file of {pdf_file_path}")

# pdf_to_path("data/microwave/user_manual/manual.pdf", "data/microwave/user_manual/manual.txt")

#############################################
#
#
# Method: Use GPT-4o to infer Text from PDF
#
#
#############################################




def create_backup(path):
    backup_path = ".".join(path.split(".")[:-1]) + "_backup." + path.split(".")[-1] if len(path.split(".")) > 1 else path + "_backup"
    with file_lock:
        if os.path.exists(backup_path):
            if os.path.isdir(backup_path):
                shutil.rmtree(backup_path)
            elif os.path.isfile(backup_path):
                os.remove(backup_path)
        if os.path.isdir(path):
            shutil.copytree(path, backup_path)
        else:
            shutil.copy2(path, backup_path)
    print(f"Backup of '{path}' created as '{backup_path}'.")

def extract_page_number(filename):
    match = re.search(r'page_(\d+)', filename)
    return int(match.group(1)) if match else None

def create_or_replace_path(path):
    
    # Create a backup if the path exists
    if os.path.exists(path):
        create_backup(path)

    # Check if the path is a directory
    if os.path.isdir(path):
        # Remove the directory if it exists
        shutil.rmtree(path)
        print(f"Existing directory '{path}' and all its contents have been deleted.")
        
        # Recreate the directory
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")

    # Check if the path is a file
    elif os.path.isfile(path):
        # Remove the file if it exists
        os.remove(path)
        print(f"Existing file '{path}' has been deleted.")
        
        # Ensure the directory of the file exists before creating the file
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Directory '{directory}' created successfully.")

        # Create a new file
        with open(path, 'w') as file:
            file.write("")  # Write an empty string (creating an empty file)
            print(f"New file '{path}' created.")

    # If the path does not exist at all
    else:
        directory = os.path.dirname(path)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Directory '{directory}' created successfully.")

def convert_pdf_to_images(pdf_path, image_folder_path, zoom=8):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Ensure the output folder exists
    if not os.path.exists(image_folder_path):
        os.makedirs(image_folder_path)

    # Loop through each page
    for page_number in range(len(pdf_document)):
        # Get the page
        
        page = pdf_document.load_page(page_number)
       
        mat = fitz.Matrix(zoom, zoom)
        # Render page to an image with the zoom matrix
        pix = page.get_pixmap(matrix=mat,  alpha=False, annots=True, colorspace=fitz.csRGB)
        
        output_image_path = os.path.join(image_folder_path, f"page_{page_number + 1}.jpg")
        pix.pil_save(output_image_path)
    return image_folder_path


def resize_image_to_temp(image_path, max_size=(1024, 1024), quality=85):
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img.thumbnail(max_size, Image.LANCZOS)
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img.save(temp_file.name, format='JPEG', quality=quality)
        return temp_file.name

def extract_text_from_image(image_files, output_text_path, prompt, max_retries=3):
    create_or_replace_path(output_text_path)
    with open(output_text_path, "w") as output_text_file:
        print(output_text_path)

        for i, image_file in enumerate(image_files):
            try:
                # Resize image to temporary path
                temp_image_path = resize_image_to_temp(image_file)

                # Run GPT-4o on the resized image
                model = GPT4O()
                extracted_text = model.chat(prompt, temp_image_path)

                output_text_file.write(extracted_text + "\n\n")
                output_text_file.flush()
                print(f"Finished {image_file}")
            except Exception as e:
                print(f"Error processing {image_file}: {e}")
            finally:
                # Delete temporary resized image
                if os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
        

def batch_convert_pdf_to_images(pdf_file_path = "/data/home/jian/RLS_microwave/benchmark/user_manual", image_folder_path = "/data/home/jian/RLS_microwave/benchmark/user_manual_images"):

    # Iterate through all directories in the user_manual folder
    for root, dirs, files in os.walk(pdf_file_path):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            print(f"Directory: {dir_path}")
            # List all files in the current directory
            for file in os.listdir(dir_path):
                print(f"direcotry: {directory}, file: {file}")
                if any(s in directory for s in ["washing_machine", "rice_cooker"]):
                    continue
                # if not "_1_dehumidifier/_3.txt" in save_text_path and not "_6_washing_machine/_5.txt" in save_text_path 
                file_path = os.path.join(dir_path, file)
                print(f"  File: {file_path}")
                # Check if the file is a PDF
                if file_path.endswith(".pdf"):
                    # Convert the PDF to images
                    image_folder_name = file_path.split("/")[-1].replace(".pdf", "_images")
                    image_file_path = os.path.join(os.path.join(image_folder_path, directory), image_folder_name)
                    
                    output_image_folder_path = convert_pdf_to_images(file_path, image_file_path)
                    print(f"Images saved to: {output_image_folder_path}")
                    

def load_image_files(image_folder_path):
    image_files = [os.path.join(image_folder_path, f) for f in os.listdir(image_folder_path) if os.path.isfile(os.path.join(image_folder_path, f))]
    image_files = sorted(image_files, key=extract_page_number)
    return image_files



def run_gpt_4o(image_folder_path, user_manual_text_path):
    prompt = """
    Can you extract the texts from this image? The document translation should be word-for-word, ensuring that no words are missed. 

    Please include any graphic symbols in the main text paragraph, replacing them with their corresponding descriptions or explanations. For example, If you see arrows, convert it into "up arrow" or "down arrow" accordingly. Other example symbols include start, next, stop, play, pause, fast forward, rewind, radio, etc.

    Please format the table text in a readable way. If you're formatting a table that lists items along with their categories where the category name would usually span multiple rows (merged cells), instead, include the category name in every row under the category column. For instance, if you have a category 'Fruits' with items 'Apple' and 'Banana', format it like this:

        | Category | Item  |
        |----------|-------|
        | Fruits   | Apple |
        | Fruits   | Banana|
    
    """

    image_files = load_image_files(image_folder_path)

    print(f"all images: {image_files}")

    extract_text_from_image(image_files, user_manual_text_path, prompt)

def batch_run_gpt_4o(image_folder_path, user_manual_text_path):
    os.makedirs(user_manual_text_path, exist_ok=True)
    machine_type_dirs = [os.path.join(image_folder_path, d) for d in os.listdir(image_folder_path) if os.path.isdir(os.path.join(image_folder_path, d))]
        
    for dir1 in machine_type_dirs:
        # List all subdirectories in each level one directory
        machine_id_dirs = [os.path.join(dir1, d) for d in os.listdir(dir1) if os.path.isdir(os.path.join(dir1, d))]
        
        relative_path = os.path.relpath(dir1, image_folder_path)
        save_text_dir = os.path.join(user_manual_text_path, relative_path) 
            
        for dir2 in machine_id_dirs:
            
            id_name = dir2.split("/")[-1].split("_")[0]
            save_text_path = os.path.join(save_text_dir, "_" + id_name + ".txt")
            #print(f"save text path: {save_text_path}")
            if any(s in save_text_path for s in ["_1_washing_machine", "_2_rice_cooker", "_4_water_dispenser", "_5_induction_cooker"]):
                continue 
            #if not any(s in save_text_path for s in ["_2_bottle_washer/_1.txt", "_2_bottle_washer/_4.txt", "_4_microwave_oven/_2.txt" ]):
            #    continue
            run_gpt_4o(dir2, save_text_path)
            

if __name__ == "__main__":

    # srun -u -o "log.out" -w crane5 --mem=20000 --gres=gpu:1 --cpus-per-task=8 --job-name “t2a” python3 

    #######################################
    #
    # Convert PDF to Images
    #
    #######################################

    pdf_file_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_0_pdf')
    image_folder_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_1_images')
    user_manual_text_path = os.path.expanduser('~/TextToActions/datasetv2/real_world/_1_user_manual/_2_text')
    #batch_convert_pdf_to_images(pdf_file_path, image_folder_path)

    #######################################
    #
    # Run GPT-4o on Images to Extract Text
    #
    #######################################

    batch_run_gpt_4o(image_folder_path, user_manual_text_path)

    #######################################
    #
    # Text Extraction on a single manual 
    #
    ######################################
    pdf_path =os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_0_pdf/_6_coffee_machine/_0.pdf')
    image_folder_path = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_1_images/_6_coffee_machine/_0_images')
    user_manual_text_path = os.path.expanduser('~/TextToActions/dataset/simulated/_1_user_manual/_2_text/_6_coffee_machine/_0.txt')
    #convert_pdf_to_images(pdf_path, image_folder_path)
    #convert_pdf_to_images(pdf_path, image_folder_path, zoom=4)
    #run_gpt_4o(image_folder_path, user_manual_text_path)




