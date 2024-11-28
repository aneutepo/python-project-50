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
	poetry run flake8 gendiff/scripts/generate_diff.py

	 
	 
gotests:
	poetry run pytest
	