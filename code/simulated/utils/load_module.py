import importlib.util
import os

def load_module(filepath, classnames=None):
    """
    Load a Python module dynamically from a given filepath and inject specified classnames into its namespace.
    """
    spec = importlib.util.spec_from_file_location(os.path.basename(filepath), filepath)
    module = importlib.util.module_from_spec(spec)
    
    
    # Inject classes into the module's namespace if classnames are provided
    if classnames:
        for classname in classnames:
            if classname in globals():
                setattr(module, classname, globals()[classname])
            else:
                print(f"Class '{classname}' not found in the global namespace.")
    
    # Execute the module after injection
    spec.loader.exec_module(module)
    return module

def load_modules(filepaths, classnames=None):
    modules = []
    for filepath in filepaths:
        # Pass the classnames to load_module so that they can be injected
        modules.append(load_module(filepath, classnames))
    return modules
