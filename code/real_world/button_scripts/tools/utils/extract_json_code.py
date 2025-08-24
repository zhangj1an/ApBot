import re
def extract_json_code(input_text):
    # Regular expression to match Python code
    if '```' in input_text:
        code_pattern = re.compile(r'```json(.*?)```', re.DOTALL)
        code_matches = code_pattern.findall(input_text)
        
        # Combine all the code blocks into one string
        extracted_code = "\n".join(code_matches).strip()
    
        return extracted_code
    else:
        return input_text