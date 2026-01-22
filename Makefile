.PHONY: install serve build

install:
	pip install -e .

serve:
	mkdocs serve

build:
	mkdocs build --strict

