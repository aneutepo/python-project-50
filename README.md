### Hexlet tests and linter status:
[![Actions Status](https://github.com/aneutepo/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aneutepo/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/a8026325a98787d6136a/maintainability)](https://codeclimate.com/github/aneutepo/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a8026325a98787d6136a/test_coverage)](https://codeclimate.com/github/aneutepo/python-project-50/test_coverage)


# gendiff

## Описание
**gendiff** — утилита для сравнения двух конфигурационных файлов и вывода их различий.

## Использование
gendiff -h
Выведет справочную информацию:
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments: first_file second_file

optional arguments: -h, --help show this help message and exit


## Установка
Утилита написана на Python и использует модуль `argparse` для обработки аргументов командной строки. Чтобы использовать её, убедитесь, что у вас установлен Python 3.

## Пример работы
gendiff file1.json file2.json

Выведет различия между `file1.json` и `file2.json` в удобном формате.

## Команды
| Команда | Описание |
|---------|----------|
| `poetry install` | Установить зависимости |
| `poetry shell` | Активировать виртуальное окружение |
| `git add .` | Добавить все изменения в Git |
| `git commit -m "add new configurate files and functions"` | Закоммитить изменения |
| `git push` | Отправить изменения в удалённый репозиторий |
| `clear` | Очистить консоль |
| `poetry build` | Собрать проект |
| `poetry run flake8 gendiff/scripts/generate_diff.py` | Запустить линтер |
| `poetry run pytest` | Запустить тесты |
| `poetry run pytest --cov=gendiff --cov-report xml` | Запустить тесты с покрытием |

## Зависимости
- Python 3.x
- Модуль `argparse` (входит в стандартную библиотеку Python)


