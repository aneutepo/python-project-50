import argparse
from gendiff.scripts.generate_diff import start_calculate


def parsepaths():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description=(
            "Compares two configuration files and shows a difference."
        )
    )
    # Аргументы
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    # Optional
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    start_calculate(args.first_file, args.second_file)


if __name__ == "__main__":
    parsepaths()
