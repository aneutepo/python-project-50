import json
import yaml


# Функция открытия файлов и сортировка их содержимого
def open_files(filepath1, filepath2):
    if filepath1.split('.') == 'json' and filepath2.split('.') == 'json':
        f1 = json.load(open(filepath1))
        f2 = json.load(open(filepath2))
    else:
        f1 = yaml.safe_load(open(filepath1))
        f2 = yaml.safe_load(open(filepath2))
    f1 = dict(sorted(f1.items()))
    f2 = dict(sorted(f2.items()))
    return (f1, f2)


def calculate_differences(file1, file2):
    result = {}
    new_keys_in_file2 = set(file2) - set(file1)

    for key, value in file1.items():
        if key in file2:
            if value == file2[key]:
                result[key] = value
            else:
                result[f"- {key}"] = value
                result[f"+ {key}"] = file2[key]
        else:
            result[f"- {key}"] = value

    for key in new_keys_in_file2:
        result[f"+ {key}"] = file2[key]
    return dict(sorted(result.items(), key=lambda item: item[0].lstrip('+- ')))


def start_calculate(path1, path2):
    f1, f2 = open_files(path1, path2)
    result = calculate_differences(f1, f2,)
    print(result)
    return result
