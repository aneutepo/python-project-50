"""Comparing two flat json files."""

import json
import yaml
from format.plain import plain
from format.stylish import keys_recovery, format_dict
from format.json import format_json


def file_opener(file_path):
    """Opening some json file."""
    with open(file_path, 'r') as file:
        if file_path[-4:] == 'json':
            return json.load(file)
        if file_path[-4:] == 'yaml' or file_path[-4:] == '.yml':
            return yaml.safe_load(file)


def generate_diff(path1, path2, format_name='stylish'):
    """A main function which creates a comparison of two flat json files."""
    data1 = prepare(file_opener(path1))
    data2 = prepare(file_opener(path2))
    diff = structure(data1, data2)
    if format_name == 'stylish':
        return format_dict(keys_recovery(diff))
    elif format_name == 'plain':
        return plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        return ('"format_name" is not applicable, '
                'please enter a valid format name')


def structure(first_dict, second_dict):
    diff_dict = {}
    common = set(first_dict).intersection(set(second_dict))

    # Сравнение общих элементов
    if common:
        for item in common:
            first_value = first_dict[item]
            second_value = second_dict[item]
            # Проверка на равенство значений, включая None
            if first_value == second_value:
                diff_dict[f'  =={item[4:]}'] = first_value
            else:
                if (isinstance(first_value, dict)
                   and isinstance(second_value, dict)):
                    diff_dict[f'{item}'] = structure(first_value, second_value)
                else:
                    if first_value != second_value:
                        if item in first_dict:
                            diff_dict[f'  --{item[4:]}'] = first_value
                        if item in second_dict:
                            diff_dict[f'  ++{item[4:]}'] = second_value

# Сравнение оставшихся элементов
    leftovers = set(first_dict).symmetric_difference(set(second_dict))
    if leftovers:
        for item in leftovers:
            if item in first_dict:
                diff_dict[f'  - {item[4:]}'] = first_dict[item]
            if item in second_dict:
                diff_dict[f'  + {item[4:]}'] = second_dict[item]

    # Сортировка результатов
    d_sorted = dict(
        sorted(
            diff_dict.items(),
            key=lambda x: (x[0][4:])
        )
    )
    return d_sorted


def prepare(some_dict):
    prepared = {}
    for key, val in some_dict.items():
        if isinstance(val, dict):
            prepared[f'    {key}'] = prepare(val)
        else:
            prepared[f'    {key}'] = val
    return prepared
