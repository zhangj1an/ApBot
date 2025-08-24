import sys
sys.path.append("/data/home/jian/TextToActions/code")
from simulated.utils.load_module import load_module
from simulated.utils.load_string_from_file import load_string_from_files

import sys
import os

def load_class_from_files(imported_files, classname, namespace, import_statements):
    """
    Load a specific class from a given string of code and inject it into the provided namespace.
    """
    

    code_string = load_string_from_files(imported_files)
    code_string = import_statements + "\n" + code_string
    # Compile the code string into an executable module
    compiled_code = compile(code_string, '<string>', 'exec')

    # Execute the compiled code in the provided namespace
    exec(compiled_code, namespace)

    try:
        # Try to get the class from the namespace
        class_obj = namespace[classname]
        return class_obj
    except KeyError:
        # Class not found in the namespace, return None
        print(f"Class '{classname}' not found in the provided code.")
        return None

def load_classes_from_files(imported_files, classnames):
    """
    Load multiple classes from a given list of files and inject all matching classes into the global namespace.
    
    :param imported_files: List of file paths to load the classes from.
    :param classnames: List of class names to look for in the files.
    :param import_statements: String of import statements needed for the code execution.
    """
    
    for filename in imported_files:
        namespace = {}
        
        # Load the code from the file
        code_string = load_string_from_files([filename])
        
        # Compile the code string into an executable module
        compiled_code = compile(code_string, '<string>', 'exec')
        
        # Execute the compiled code in the temporary namespace
        exec(compiled_code, globals())
        
        # Check each class name in classnames to see if it's in the namespace
        for classname in classnames:
            if classname in globals():
                # Add the class to the global namespace
                #globals()[classname] = namespace[classname]
                print(f"Class '{classname}' from file '{filename}' successfully added to globals.")
            #else:
                #print(f"Class '{classname}' not found in file '{filename}'.")


if __name__ == "__main__":
    # Example usage
    import_files = ['path/to/file1.py', 'path/to/file2.py']
    classnames = ['AClass', 'BClass']

    # Load the classes from the files into a custom namespace
    custom_namespace = {}
    load_class_from_files(import_files, classnames, custom_namespace)

    # Now you can instantiate the classes directly from the custom namespace
    a = custom_namespace['AClass']()  # Assuming AClass is defined in one of the files
    b = custom_namespace['BClass']()  # Assuming BClass is defined in another file
