SHELL := /bin/bash

create:
	python3 -m venv .venv
run: #Ejecuta tanto el venv como el main
	source .venv/bin/activate && python3 main.py
install:
	.venv/bin/pip install -r requirements.txt
typecheck: #Chequeos estaticos, aun no hay ninguno
	mypy main.py
	mypy processing/
test: #  aun no he implementado un test particular.
	python -m unittest discover -s tests
