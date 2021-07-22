.PHONY: setup \
	run \
	db \
	createsuperuser \
	black \
	flake8 \
	mypy \

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate ## run project
	. venv/bin/activate; python entry.py -c ./local.yaml --reload

black: venv/bin/activate ## Format code with black
	. venv/bin/activate; black ./

flake8: venv/bin/activate ## Flake8 codestyle
	. venv/bin/activate; flake8 ./

mypy: venv/bin/activate ## Type checking
	. venv/bin/activate; mypy ./
	
