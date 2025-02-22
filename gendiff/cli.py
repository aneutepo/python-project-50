import argparse
from pathlib import Path
from gendiff.generate_diff import generate_diff


def parsepaths():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    # Аргументы
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    # Опциональные аргументы
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    args = parser.parse_args()

    # Определяем путь к текущей директории (где находится скрипт)
    current_dir = Path(__file__).parent

    # Формируем абсолютные пути к файлам в папке 'fixtures'
    path1 = current_dir / 'tests' / 'fixtures' / args.first_file
    path2 = current_dir / 'tests' / 'fixtures' / args.second_file

    # Вызов основной функции для расчета различий
    diff = generate_diff(path1, path2, args.format)
    print(diff)


if __name__ == "__main__":
    parsepaths()
