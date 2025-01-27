from gendiff.generate_diff import start_calculate
import os
import json


def test_calculating():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2)

    etalon = {'- follow': False,
              'host': 'hexlet.io',
              '- proxy': '123.234.53.22',
              '- timeout': 50,
              '+ timeout': 20,
              '+ verbose': True
              }
    assert result == etalon


def test_calculating1():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2, format_type='plain')
    etalon = ("Property 'follow' was removed\n"
              "Property 'proxy' was removed\n"
              "Property 'timeout' was removed\n"
              "Property 'timeout' was added\n"
              "Property 'verbose' was added")  
    assert result == etalon


def test_calculating_json():
    current_directory = os.path.dirname(__file__)
    path1 = os.path.join(current_directory, 'fixtures', "file1.json")
    path2 = os.path.join(current_directory, 'fixtures', "file2.json")
    result = start_calculate(path1, path2, format_type='json')
    etalon = {
        "- follow": False,
        "host": "hexlet.io",
        "- proxy": "123.234.53.22",
        "- timeout": 50,
        "+ timeout": 20,
        "+ verbose": True
    }
    assert json.loads(result) == etalon  
