import json


# Функция открытия файлов и сортировка их содержимого
def open_files(filepath1, filepath2):
    f1 = json.load(open(filepath1))
    f2 = json.load(open(filepath2))
    f1 = dict(sorted(f1.items()))
    f2 = dict(sorted(f2.items()))
    return (f1, f2)


def calculate_differences(file1, file2):
    result = {}
    deleted_list = []
    different_referenses = []
    k1 = file1.keys()
    k2 = file2.keys()
    new_points_f1 = k2-k1
    for k1, v1 in file1.items():
        if file2.get(k1, 0):
            if file1[k1] == file2[k1]:
                result[k1] = file2[k1]
            else:
                different_referenses.append(file2[k1])
                result[f"- {k1}"] = file1[k1]
                result[f"+ {k1}"] = file2[k1]
        else:
            deleted_list.append(k1)
            result[f"- {k1}"] = file1[k1]

        for i in new_points_f1:
            result[f"+ {i}"] = file2[i]
    result = dict(sorted(
        result.items(), key=lambda item: item[0].lstrip('+- ')))
    return result


def start_calculate(path1, path2):
    f1, f2 = open_files(path1, path2)
    result = calculate_differences(f1, f2)
    print(result)
