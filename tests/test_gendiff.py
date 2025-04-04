import pytest
from gendiff import engine

json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yml"
res_stylish = "tests/fixtures/result_stylish"
res_plain = "tests/fixtures/result_plain"
res_json = "tests/fixtures/result_json.json"

formats = ["stylish", "plain", "json"]


@pytest.mark.parametrize(
    "path1, path2, format_name, expected",
    [
        (json_1, json_2, formats[0], res_stylish),
        (yaml_1, yaml_2, formats[0], res_stylish),
        (json_1, json_2, formats[1], res_plain),
        (yaml_1, yaml_2, formats[1], res_plain),
        (json_1, json_2, formats[2], res_json),
        (yaml_1, yaml_2, formats[2], res_json),
    ],
)
def test_generate_diff(path1, path2, format_name, expected):
    with open(expected) as f:
        assert engine.generate_diff(path1, path2, format_name) == f.read()
