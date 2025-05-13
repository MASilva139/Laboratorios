# Variables
VENV = venv
PYTHON = $(VENV)/Scripts/python
PIP = $(VENV)/Scripts/pip
PYTEST = $(VENV)/Scripts/pytest

# Crear ambiente virtual
venv:
	python -m venv $(VENV)

# Instalar dependencias
install: venv
	$(PIP) install -r requirements.txt

# Ejecutar tests
test:
	$(PYTEST) tests/

# Ejecutar chequeos estáticos con pylint
lint:
	$(PYTHON) -m pylint processing/ main.py

# Ejecutar la simulación
run:
	$(PYTHON) main.py

# Limpiar archivos generados
clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

.PHONY: venv install test lint run clean
