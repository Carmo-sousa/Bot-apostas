.DEFAULT_GOAL := help

PEP8 		:= flake8
BLACK 		:= black
MYPY 		:= mypy
PYLINT 		:= pylint

pep8:
	$(PEP8) --show-source score_bing app.py

black:
	$(BLACK) .

mypy:
	$(MYPY) score_bing app.py

all: pep8 black mypy

help:
	@echo "Available targets:"
	@echo "- pep8        Check style with flake8"
	@echo "- black       Check style with black"
	@echo "- mypy        Check type hinting with mypy"
	@echo "- all         Run all"
