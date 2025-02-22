install:
	poetry install
	poetry shell


git:
	git add .
	git commit -m "add new configurate files and functions"
	git push
	clear

build:
	poetry build


lint:
	poetry run flake8 gendiff/generate_diff.py
	poetry run flake8 gendiff/cli.py
	poetry run flake8 tests/test_calculate_differense.py
	poetry run flake8 tests/test_openfiles.py

gotests:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff --cov-report xml