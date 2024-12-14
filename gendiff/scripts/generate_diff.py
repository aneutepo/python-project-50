import json
import yaml


# Функция открытия файлов и сортировка их содержимого
def open_files(filepath1, filepath2):
    with open(filepath1, 'r') as file1, open(filepath2, 'r') as file2:
        if filepath1.endswith('.json') and filepath2.endswith('.json'):
            f1 = json.load(file1)
            f2 = json.load(file2)
        else:
            f1 = yaml.safe_load(file1)
            f2 = yaml.safe_load(file2)

    return f1, f2


# Функция для обработки различий одного ключа
def handle_key_diff(key, file1, file2, result):
    if key in file1 and key in file2:
        if isinstance(file1[key], dict) and isinstance(file2[key], dict):
            # Рекурсивное сравнение вложенных структур
            result[key] = calculate_differences(file1[key], file2[key])
        elif file1[key] == file2[key]:
            # Значения равны
            result[key] = file1[key]
        else:
            # Значения различаются
            result[f"- {key}"] = file1[key]
            result[f"+ {key}"] = file2[key]
    elif key in file1:
        # Ключ только в первом файле
        result[f"- {key}"] = file1[key]
    elif key in file2:
        # Ключ только во втором файле
        result[f"+ {key}"] = file2[key]


# Основная функция для вычисления различий
def calculate_differences(file1, file2):
    result = {}
    all_keys = sorted(set(file1.keys()).union(file2.keys()))

    for key in all_keys:
        handle_key_diff(key, file1, file2, result)

    return result


# Функция для запуска
def start_calculate(path1, path2, format_type='stylish'):
    f1, f2 = open_files(path1, path2)
    result = calculate_differences(f1, f2)

    # Выбираем формат вывода
    if format_type == 'plain':
        return format_plain(result)  # строка
    elif format_type == 'json':
        return format_json(result)  # вывод в JSON
    else:
        return format_stylish(result)  # возвращаем как есть (словарь)


def format_json(result):
    return json.dumps(result, indent=4)


def format_plain(result):
    formatted = ""
    for key, value in result.items():
        if isinstance(value, dict):
            formatted += (f"Property '{key}' was updated. "
                          f"From {value['-']} to {value['+']}\n")
        else:
            if key.startswith("- "):
                formatted += f"Property '{key[2:]}' was removed\n"
            elif key.startswith("+ "):
                formatted += f"Property '{key[2:]}' was added\n"

    return formatted.strip()


# Форматирование результата для вывода в "стильном" формате
def format_stylish(result, indent=0):
    formatted = {}
    for key, value in result.items():
        if isinstance(value, dict):  # Если значение - вложенный словарь
            formatted[key] = format_stylish(value, indent + 4)
        else:  # Если значение - не словарь
            formatted[key] = value
    return formatted
