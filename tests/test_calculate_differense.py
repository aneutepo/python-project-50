from gendiff.generate_diff import start_calculate
import os
import json


def test_calculating():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2)
    etalon_path = os.path.join(
        current_directory,
        'fixtures',
        'etalon_start_calc.json'
    )
    with open(etalon_path, 'r') as etalon_file:
        expected_result = json.load(etalon_file)
    assert result == expected_result


def test_calculating1():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2, format_type='plain')
    etalon_path = os.path.join(current_directory, 'fixtures', 'etalon1.txt')
    with open(etalon_path, 'r') as etalon_file:
        expected_result = etalon_file.read()
    assert result == expected_result


def test_calculating_json():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2, format_type='json')
    etalon_path = os.path.join(
        current_directory, 'fixtures', 'etalon_test_calculating_json.json'
    )
    with open(etalon_path, 'r') as etalon_file:
        expected_result = json.load(etalon_file)
    assert json.loads(result) == expected_result
