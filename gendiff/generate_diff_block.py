import json
import yaml


def open_files(filepath1, filepath2):
    with open(filepath1, 'r') as file1, open(filepath2, 'r') as file2:
        # Проверяем, если хотя бы один из файлов в формате JSON
        if filepath1.endswith('.json') or filepath2.endswith('.json'):
            f1 = json.load(file1)
            f2 = json.load(file2)
        else:
            # Если файлы не JSON, то загружаем их как YAML
            f1 = yaml.safe_load(file1)
            f2 = yaml.safe_load(file2)
    return f1, f2


def handle_key_diff(key, file1, file2, result):
    if key in file1 and key in file2:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = calculate_differences(file1[key], file2[key])
        elif normalize_value(file1[key]) == normalize_value(file2[key]):
            result[key] = file1[key]
        else:
            result[f"- {key}"] = file1[key]
            result[f"+ {key}"] = file2[key]
    elif key in file1:
        result[f"- {key}"] = file1[key]
    elif key in file2:
        result[f"+ {key}"] = file2[key]


def normalize_value(value):
    """Приводим значение к стандартному виду для сравнения."""
    if isinstance(value, bool):
        return str(value).lower()  # Преобразуем в 'true' или 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, float):
        return str(value)
    return value


def calculate_differences(file1, file2):
    result = {}
    all_keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in all_keys:
        handle_key_diff(key, file1, file2, result)
    return result


def format_json(result):
    return json.dumps(result, indent=4)


def format_plain(result):
    formatted = []
    for key, value in result.items():
        if isinstance(value, dict):
            if "-" in value and "+" in value:
                formatted.append(
                    f"Property '{key}' was updated. "
                    f"From {value['-']} to {value['+']}"
                )
        else:
            if key.startswith("- "):
                formatted.append(f"Property '{key[2:]}' was removed")
            elif key.startswith("+ "):
                formatted.append(f"Property '{key[2:]}' was added")
    return "\n".join(formatted)


def format_stylish(result, indent=0):
    formatted = ""
    for key, value in result.items():
        indent_str = " " * indent
        if isinstance(value, dict):
            formatted += f"{indent_str}{key}: {{\n"
            formatted += format_stylish(value, indent + 4)
            formatted += f"{indent_str}}}\n"
        else:
            formatted += f"{indent_str}{key}: {value}\n"
    return formatted.strip()  # Strip any leading/trailing whitespace


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
