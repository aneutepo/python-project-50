"""
This Cli-program return differents two files
"""

from gendiff.engine import generate_diff
from gendiff.cli import parse_cli_args


def main():
    path1, path2, format_name = parse_cli_args()
    print(generate_diff(path1, path2, format_name))


if __name__ == '__main__':
    main()
