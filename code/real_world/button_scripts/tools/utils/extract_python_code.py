import re
import textwrap
def extract_python_code(input_text):
    input_text = textwrap.dedent(input_text)
    # Regular expression to match Python code
    if '```python' in input_text:
        code_pattern = re.compile(r'```(?:python)?\n(.*?)```', re.DOTALL)

        code_matches = code_pattern.findall(input_text)
        
        # Combine all the code blocks into one string
        extracted_code = "\n".join(code_matches).strip()
    
        return extracted_code
    else:
        return input_text