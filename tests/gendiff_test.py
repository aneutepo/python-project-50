from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import get_dictionary_from_file
from gendiff.scripts.gendiff import generate_diff_tree
import gendiff.formaters.stylish as stylish
import pytest
from pathlib import Path


FIXTURES_DIR = f"{Path(__file__).parent}/fixtures"


@pytest.fixture
def dictionary1():
    return {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
    }


@pytest.fixture
def dict_string_inset_1():
    return (
        "{\n        host: hexlet.io\n        timeout: 50\n"
        "        proxy: 123.234.53.22\n        follow: false\n    }"
    )


def test4():
    file1_dict = get_dictionary_from_file(f"{FIXTURES_DIR}/file1.yaml")
    assert file1_dict == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
    }


def test_yaml(dictionary1):
    file1_dict = get_dictionary_from_file(f"{FIXTURES_DIR}/file1.yml")
    assert file1_dict == dictionary1


def test_yml(dictionary1):
    file1_dict = get_dictionary_from_file(f"{FIXTURES_DIR}/file1.yml")
    assert file1_dict == dictionary1


def test5():
    diff = (
        '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n'
        '  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    )
    result = generate_diff(f"{FIXTURES_DIR}/file1.json", f"{FIXTURES_DIR}/file2.json").lower()
    assert result == diff.lower()


def test_nested():
    with open(f"{FIXTURES_DIR}/result.txt", 'r') as f:
        diff_string = generate_diff(f"{FIXTURES_DIR}/nested1.json", f"{FIXTURES_DIR}/nested2.json")
        for k, v in zip(diff_string.split('\n'), f):
            assert k.lower() == v.lower() or (k + '\n').lower() == v.lower()


def test_nested_plain():
    with open(f"{FIXTURES_DIR}/result_flat.txt", 'r') as f:
        diff_string = generate_diff(
            f"{FIXTURES_DIR}/nested1.json",
            f"{FIXTURES_DIR}/nested2.json",
            'plain'
        )
        for k, v in zip(diff_string.split('\n'), f):
            assert k.strip() == v.strip()


def test_of_dict():
    test_list = [
        (' ', 'common', [
            ('+', 'follow', False),
            (' ', 'setting1', 'Value 1'),
            ('-', 'setting2', 200),
            ('-+', 'setting3', True, 'null'),
            ('+', 'setting4', 'blah blah'),
            ('+', 'setting5', [(' ', 'key5', 'value5')]),
            (' ', 'setting6', [
                (' ', 'doge', [('-+', 'wow', '', 'so much')]),
                (' ', 'key', 'value'),
                ('+', 'ops', 'vops'),
            ]),
        ]),
        (' ', 'group1', [
            ('-+', 'baz', 'bas', 'bars'),
            (' ', 'foo', 'bar'),
            ('-+', 'nest', [(' ', 'key', 'value')], 'str'),
        ]),
    ]
    res = generate_diff_tree(
        f"{FIXTURES_DIR}/nested_short1.json",
        f"{FIXTURES_DIR}/nested_short2.json"
        )
    print(test_list)
    print(res)
    assert test_list == res


def test_of_str():
    test_tree = [
        (' ', 'key1', 'value1'),
        ('+', 'key2', [(' ', 'key3', 'value2')])
    ]
    s = '{\n    key1: value1\n  + key2: {\n        key3: value2\n    }\n}'
    assert stylish.stringify(test_tree) == s
