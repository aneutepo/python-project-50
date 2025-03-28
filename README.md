### Hexlet tests and linter status:
[![Actions Status](https://github.com/aneutepo/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aneutepo/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/a8026325a98787d6136a/maintainability)](https://codeclimate.com/github/aneutepo/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a8026325a98787d6136a/test_coverage)](https://codeclimate.com/github/aneutepo/python-project-50/test_coverage)


# gendiff

## Description
**gendiff** — a utility for comparing two configuration files and displaying their differences.

## Usage
gendiff -h
This will display help information:
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments: first_file second_file

optional arguments: -h, --help show this help message and exit


## Installation
The utility is written in Python and uses the `argparse` module for command-line argument parsing. To use it, ensure that Python 3 is installed on your system.

## Example
gendiff file1.json file2.json

This will output the differences between `file1.json` and `file2.json` in a convenient format.

## Commands
| Command | Description |
|---------|-------------|
| `poetry install` | Install dependencies |
| `poetry shell` | Activate the virtual environment |
| `git add .` | Add all changes to Git |
| `git commit -m "add new configuration files and functions"` | Commit the changes |
| `git push` | Push changes to the remote repository |
| `clear` | Clear the console |
| `poetry build` | Build the project |
| `poetry run flake8 gendiff/scripts/generate_diff.py` | Run the linter |
| `poetry run pytest` | Run the tests |
| `poetry run pytest --cov=gendiff --cov-report xml` | Run the tests with coverage |

## Dependencies
- Python 3.x
- The `argparse` module (part of the Python standard library)


