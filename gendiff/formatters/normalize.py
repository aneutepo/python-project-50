def normalize_values(file: dict) -> dict:
    """
    Changes None-type & bool-types values:
    None to 'null', True to 'true', False to 'false'.
    """
    corr_values = {None: "null", True: "true", False: "false"}

    for key, val in file.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif isinstance(val, (bool, type(None))):
            file[key] = corr_values[val]
    return file
