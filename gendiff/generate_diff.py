import json
import yaml


def open_files(filepath1, filepath2):
    with open(filepath1, 'r') as file1, open(filepath2, 'r') as file2:
        if filepath1.endswith('.json') and filepath2.endswith('.json'):
            f1 = json.load(file1)
            f2 = json.load(file2)
        else:
            f1 = yaml.safe_load(file1)
            f2 = yaml.safe_load(file2)
    return f1, f2


def handle_key_diff(key, file1, file2, result):
    if key in file1 and key in file2:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = calculate_differences(file1[key], file2[key])
        elif file1[key] == file2[key]:
            result[key] = file1[key]
        else:
            result[f"- {key}"] = file1[key]
            result[f"+ {key}"] = file2[key]
    elif key in file1:
        result[f"- {key}"] = file1[key]
    elif key in file2:
        result[f"+ {key}"] = file2[key]


def calculate_differences(file1, file2):
    result = {}
    all_keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in all_keys:
        handle_key_diff(key, file1, file2, result)
    return result


def format_json(result):
    return json.dumps(result, indent=4)


def format_plain(result):
    formatted = ""
    for key, value in result.items():
        if isinstance(value, dict):
            if "-" in value and "+" in value:
                formatted += (
                    f"Property '{key}' was updated. "
                    f"From {value['-']} to {value['+']}\n"
                )
        else:
            if key.startswith("- "):
                formatted += f"Property '{key[2:]}' was removed\n"
            elif key.startswith("+ "):
                formatted += f"Property '{key[2:]}' was added\n"
    return formatted.strip()


def format_stylish(result, indent=0):
    formatted = {}
    for key, value in result.items():
        if isinstance(value, dict):
            formatted[key] = format_stylish(value, indent + 4)
        else:
            formatted[key] = value
    return formatted


def start_calculate(path1, path2, format_type='stylish'):
    f1, f2 = open_files(path1, path2)
    result = calculate_differences(f1, f2)
    if format_type == 'plain':
        return format_plain(result)
    elif format_type == 'json':
        return format_json(result)
    else:
        return format_stylish(result)


def generate_diff(filepath1, filepath2, format_type='stylish'):
    return start_calculate(filepath1, filepath2, format_type)
