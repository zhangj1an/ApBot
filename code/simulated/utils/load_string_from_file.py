def load_string_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def load_string_from_files(filepaths):
    content = ""
    for filepath in filepaths:
        content += load_string_from_file(filepath) + "\n"
    return content