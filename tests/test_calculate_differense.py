from gendiff.scripts.generate_diff import start_calculate


def test_calculating():
    path1 = "/home/anton/python-project-50/tests/fixtures/file1.json"
    path2 = "/home/anton/python-project-50/tests/fixtures/file2.json"
    result = start_calculate(path1, path2)
    etalon = {'- follow': False,
              'host': 'hexlet.io',
              '- proxy': '123.234.53.22',
              '- timeout': 50,
              '+ timeout': 20,
              '+ verbose': True
              }
    assert result == etalon
