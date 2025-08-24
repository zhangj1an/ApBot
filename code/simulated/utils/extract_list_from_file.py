import ast

# Function to extract the list from the file content
def extract_list_from_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Parse the file content into an AST
    parsed_content = ast.parse(file_content)

    # Walk through the AST nodes to find the list or the list assigned to a variable
    for node in ast.walk(parsed_content):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and isinstance(node.value, ast.List):
                    # Extract the list node and convert it to a Python object
                    return ast.literal_eval(node.value)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.List):
            # Handle the case where the content is a direct list
            return ast.literal_eval(node.value)
    
    return None