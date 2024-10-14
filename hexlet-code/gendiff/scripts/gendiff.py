import argparse


def main():
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
    parser.parse_args()


if __name__ == "__main__":
    main()
