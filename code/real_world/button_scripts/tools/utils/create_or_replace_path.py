import shutil
import os 
import threading

file_lock = threading.Lock()

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
