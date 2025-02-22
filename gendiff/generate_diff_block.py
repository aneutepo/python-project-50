import json
import yaml


def open_files(filepath1, filepath2):
    """Открываем файлы и загружаем их содержимое в формате JSON или YAML."""
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
    """Обрабатываем различия между ключами в двух файлах."""
    if key in file1 and key in file2:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            # Рекурсивно обрабатываем вложенные словари
            result[key] = calculate_differences(file1[key], file2[key])
        elif normalize_value(file1[key]) == normalize_value(file2[key]):
            result[key] = file1[key]
        else:
            # Для различий в значениях добавляем их с префиксами
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
        return round(value, 6)  # Округляем числа с плавающей запятой
    elif isinstance(value, str):
        return value.strip().lower()
    return str(value)  # Преобразуем все остальные типы в строку для сравнения


def calculate_differences(file1, file2):
    """Рассчитываем различия между двумя файлами."""
    result = {}
    # Собираем все ключи из обоих файлов для их сравнения
    all_keys = sorted(set(file1.keys()).union(file2.keys()))
    for key in all_keys:
        handle_key_diff(key, file1, file2, result)
    return result


def format_json(result):
    """Форматируем результат в JSON."""
    return json.dumps(result, indent=4)


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


def format_stylish(result, indent=0):
    """Форматируем результат в стильный вывод."""
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
    """Запускаем процесс вычисления различий с выбором формата."""
    f1, f2 = open_files(path1, path2)
    result = calculate_differences(f1, f2)
    if format_type == 'plain':
        return format_plain(result)
    elif format_type == 'json':
        return format_json(result)
    else:
        return format_stylish(result)


def generate_diff(filepath1, filepath2, format_type='stylish'):
    """Генерируем дифф между двумя файлами."""
    return start_calculate(filepath1, filepath2, format_type)
