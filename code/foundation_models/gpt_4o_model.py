import datetime

from PIL import Image
import os
import requests

from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np
import base64
from io import BytesIO

from openai import OpenAI
#import google.generativeai as genai

# from utils.image_utils import convert_pil_image_to_base64

# OpenAI API Key
os.environ["OPENAI_API_KEY"] = ""

def convert_pil_image_to_base64(image: Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


class LanguageModel():
    def __init__(self, support_vision):
        self._support_vision = support_vision

    def support_vision(self)-> bool:
        return self._support_vision

class GPT4O(LanguageModel):
    def __init__(
        self, 
        model="gpt-4o", #"gpt-4o-turbo-2024-04-09", #"gpt-4o-mini", 
        temperature=0.0
    ):
        self.model = model
        
        self.temperature = temperature

        super().__init__(
            support_vision=True
        )

    def chat(self, prompt, image_filepath, temperature=0, top_p=0, gpt_model_type="gpt-4o",meta_prompt=""):
        #base64_image = convert_pil_image_to_base64(image)
        base64_image = encode_image(image_filepath)

        # Get OpenAI API Key from environment variable
        api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(
            api_key=api_key,
        )

        

        response = client.chat.completions.create(
            model=gpt_model_type,
            messages=[
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": meta_prompt}
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                            },
                        },
                    ],
                }
            ],
            temperature=temperature,
            max_tokens=4096,
            stream=True,

            top_p=top_p,
            timeout=300 
        )

        ret = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                ret += chunk.choices[0].delta.content
                #print(chunk.choices[0].delta.content, end="")

        #ret = response.choices[0].message.content
        return ret

    def chat_with_text(self, prompt, temperature=0, top_p=0, gpt_model_type = "gpt-4o"):
        # Get OpenAI API Key from environment variable

        try:
                api_key = os.environ["OPENAI_API_KEY"]
                client = OpenAI(
                    api_key=api_key,
                )
                response = client.chat.completions.create(
                model=gpt_model_type, #"gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt},
                    #{"role": "user", "content": control_panel_prompt},
                ],
                response_format={
                    "type": "text"
                },

                temperature=temperature,
                #max_completion_tokens=2048,
                top_p=top_p,
                #frequency_penalty=0,
                #presence_penalty=0,
                )

                answer = response.choices[0].message.content
                return answer
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

        
    
    def chat_with_context(self, context, new_message, conversation_history, context_window = 20, gpt_model_type = "gpt-4o"):

        api_key = os.environ["OPENAI_API_KEY"]
        client = OpenAI(
            api_key=api_key,
        )
        if conversation_history is None:
            conversation_history = []

        if new_message is not None:
            # Append new message to the conversation history
            conversation_history.append({"role": "user", "content": new_message})

        if len(conversation_history) > context_window:
            conversation_history.pop(0)  # Remove the oldest message


        # Make the API call with the combined context and conversation history
         
        response = client.chat.completions.create(
            model=gpt_model_type, #"gpt-4o",
            messages=[{"role": "system", "content": context}] + conversation_history
        )

        answer = response.choices[0].message.content
        # Append the model's response to the conversation history
        conversation_history.append({"role": "assistant", "content": answer})

        
        # Return the model's response
        return answer, conversation_history
        pass 
    
    def chat_with_multiple_images_and_context(self, context, new_message, conversation_history,  image_filepaths, gpt_model_type = "gpt-4o", context_window = 20, temperature = 1.0): 

        base64_images = [encode_image(image_filepath) for image_filepath in image_filepaths]

        # Get OpenAI API Key from environment variable
        api_key = os.environ["OPENAI_API_KEY"]
                
        client = OpenAI(
            api_key=api_key,
        )

        setup_content = [{"type": "text", "text": context}]

        setup_content.extend([{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}} for base64_image in base64_images])

        if conversation_history is None:
            conversation_history = [] 
        
        if new_message is not None:
            # Append new message to the conversation history
            conversation_history.append({"role": "user", "content": new_message})
        
        if len(conversation_history) > context_window:
            conversation_history.pop(0)
        
        

        response = client.chat.completions.create(
            model= gpt_model_type, #"gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": setup_content,
                }
            ] + conversation_history,
            #temperature=self.temperature,
            #max_tokens=4096,
            stream=True,
            #top_p=0,
            #timeout=300 
        )
        ret = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                ret += chunk.choices[0].delta.content

        conversation_history.append({"role": "assistant", "content": ret})
        return ret, conversation_history
        #ret = response.choices[0].message.content
        #return ret
    


    def chat_with_multiple_images(self, prompt, image_filepaths, gpt_model_type = "gpt-4o", temperature = 0, top_p=0): 

        base64_images = [encode_image(image_filepath) for image_filepath in image_filepaths]

        # Get OpenAI API Key from environment variable
        api_key = os.environ["OPENAI_API_KEY"]
                
        client = OpenAI(
            api_key=api_key,
        )

        content = [{"type": "text", "text": prompt}]

        content.extend([{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}} for base64_image in base64_images])

        response = client.chat.completions.create(
            model= gpt_model_type, #"gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            temperature=temperature,
            max_tokens=4096,
            stream=True,
            top_p=top_p,
            timeout=300 
        )
        ret = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                ret += chunk.choices[0].delta.content

        return ret
        #ret = response.choices[0].message.content
        #return ret
    
if __name__ == "__main__":
    # Path to your image
    image_path = "/data/home/jian/RLS_microwave/reasoning/rls_data/microwave/user_manual/images/page_14.jpg"
    prompt = """
    Can you extract the texts from this image? The document translation should be word-for-word, ensuring that no words are missed. 

    Please include any graphic symbols in the main text paragraph, replacing them with their corresponding descriptions or explanations. If you see arrows, convert it into "up arrow" or "down arrow" accordingly.

    Please format the table text in a readable way. If you're formatting a table that lists items along with their categories where the category name would usually span multiple rows (merged cells), instead, include the category name in every row under the category column. For instance, if you have a category 'Fruits' with items 'Apple' and 'Banana', format it like this:

    | Category | Item  |
    |----------|-------|
    | Fruits   | Apple |
    | Fruits   | Banana|
    """

    #model = GPT4O()
    #response = model.chat(prompt, image_path)
    #print(response)

