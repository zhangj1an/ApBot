def replace_placeholder_in_filepaths(filepaths, placeholder, replacement):
    """
    Recursively replaces a placeholder in filepaths dictionary with the given replacement.
    
    :param filepaths: Dictionary containing file paths, possibly nested.
    :param placeholder: The string to be replaced.
    :param replacement: The string to replace the placeholder with.
    :return: A new dictionary with updated file paths.
    """
    return {
        key: (
            {
                sub_key: sub_value.replace(placeholder, replacement)
                for sub_key, sub_value in value.items()
            } if isinstance(value, dict) else value.replace(placeholder, replacement)
        )
        for key, value in filepaths.items()
    }