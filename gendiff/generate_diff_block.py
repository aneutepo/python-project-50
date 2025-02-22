import json
import yaml


def open_files(filepath1, filepath2):
    """Открываем файлы и загружаем их содержимое в формате JSON или YAML."""
    with open(filepath1, 'r') as file1, open(filepath2, 'r') as file2:
        if filepath1.endswith('.json') or filepath2.endswith('.json'):
            f1 = json.load(file1)
            f2 = json.load(file2)
        else:
            f1 = yaml.safe_load(file1)
            f2 = yaml.safe_load(file2)
    return f1, f2


def normalize_value(value):
    """Приводим значение к стандартному виду для сравнения."""
    if isinstance(value, bool):
        return str(value).lower()  # Преобразуем в 'true' или 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return value
    elif isinstance(value, str):
        return value
    return str(value)  # Преобразуем все остальные типы в строку для сравнения


def calculate_differences(file1, file2):
    """Рассчитываем различия между двумя файлами."""
    result = {}
    all_keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in all_keys:
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
    return result


def format_stylish(result, indent=2):
    """Форматируем результат в стильный вывод."""
    lines = []
    for key, value in result.items():
        if isinstance(value, dict):
            lines.append(f"{' ' * indent}{key}: {{")
            lines.append(format_stylish(value, indent + 4))
            lines.append(f"{' ' * indent}}}")
        else:
            lines.append(f"{' ' * indent}{key}: {value}")
    return "\n".join(lines)


def generate_diff(filepath1, filepath2, format_type='stylish'):
    """Генерируем дифф между двумя файлами."""
    f1, f2 = open_files(filepath1, filepath2)
    result = calculate_differences(f1, f2)
    if format_type == 'stylish':
        return "{\n" + format_stylish(result) + "\n}"
    elif format_type == 'plain':
        return format_plain(result)
    elif format_type == 'json':
        return json.dumps(result, indent=4)
    else:
        raise ValueError(f"Unknown format type: {format_type}")


def format_plain(result):
    """Форматируем результат в plain текст."""
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
