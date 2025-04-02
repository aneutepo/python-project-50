import json


from gendiff.formatters.normalize import normalize_values


def format(diff: dict) -> str:
    """
    Main function json format output.
    diff (dict): dict with differences
    return: json format data
    """
    diff = normalize_values(diff)
    return json.dumps(diff, indent=4)
