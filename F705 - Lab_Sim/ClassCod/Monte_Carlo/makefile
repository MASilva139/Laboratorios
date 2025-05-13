SHELL := /bin/bash

banner:
	@echo "  ██████████   █████████  ███████████ ██████   ██████"
	@echo " ░░███░░░░░█  ███░░░░░███░░███░░░░░░█░░██████ ██████ "
	@echo "  ░███  █ ░  ███     ░░░  ░███   █ ░  ░███░█████░███ "
	@echo "  ░██████   ░███          ░███████    ░███░░███ ░███ "
	@echo "  ░███░░█   ░███          ░███░░░█    ░███ ░░░  ░███ "
	@echo "  ░███ ░   █░░███     ███ ░███  ░     ░███      ░███ "
	@echo " ██████████ ░░█████████  █████       █████     ██████"
	@echo "░░░░░░░░░░   ░░░░░░░░░  ░░░░░       ░░░░░     ░░░░░  "

create:
	python3 -m venv .venv

run:
	source .venv/bin/activate && echo "Entorno activado (temporalmente en subshell)"

install:
	.venv/bin/pip install -r requirements.txt

typecheck:
	mypy main.py
	mypy processing/

test:
	python -m unittest discover -s tests

build: banner create run install
