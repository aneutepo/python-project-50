from gendiff.scripts.generate_diff import start_calculate
import os


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
