SHELL := /bin/bash

create:
	python3 -m venv .venv

run: #Ejecuta tanto el venv como el main
	source .venv/bin/activate && python3 main.py
	
install:
	.venv/bin/pip install -r requirements.txt

test: #  aun no he implementado un test particular.
	python -m unittest discover -s tests

# Revisión de tipos estáticos con mypy
typecheck:
	mypy main.py

ZIP_NAME=proyecto.zip
EXCLUDES=--exclude=*.pyc --exclude=__pycache__ --exclude=.venv --exclude=$(ZIP_NAME)

zip:
	zip -r $(ZIP_NAME) . $(EXCLUDES)
