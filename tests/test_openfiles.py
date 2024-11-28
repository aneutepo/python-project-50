from gendiff.scripts.generate_diff import open_files


def test_open_file1():
    path1 = "/home/anton/python-project-50/tests/fixtures/file1.json"
    path2 = "/home/anton/python-project-50/tests/fixtures/file2.json"
    file1, file2 = open_files(path1, path2)
    result1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
    }
    assert file1 == result1


def test_open_file2():
    path1 = "/home/anton/python-project-50/tests/fixtures/file1.json"
    path2 = "/home/anton/python-project-50/tests/fixtures/file2.json"
    file1, file2 = open_files(path1, path2)
    result2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    assert file2 == result2
