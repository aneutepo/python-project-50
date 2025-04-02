from gendiff.parser import convertator
from gendiff.tree import get_diff
from gendiff.formatters.formatting import formatting
import os


PREFIX_ADD = '  + '
PREFIX_DEL = '  - '
PREFIX_NCh = '    '


def read_data(path):
    """
    Open file
    """
    return open(path)


def get_format(pathfile: str) -> str:
    """
    Read filename and return extension of a file
    """
    extension = os.path.splitext(pathfile)[1].lstrip('.')
    return extension


def generate_diff(path1: str, path2: str, format_name='stylish') -> str:
    """
    Finds differences between two files
    path1 (str): pathfile to first file
    path2 (str): pathfile to second file
    format_name (str): format output data, default=stylish
    return (str): depends on param "format_name"
    """
    data1 = convertator(read_data(path1), get_format(path1))
    data2 = convertator(read_data(path2), get_format(path2))
    diff = get_diff(data1, data2)
    return formatting(diff, format_name)
