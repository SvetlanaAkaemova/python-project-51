install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page-loader tests/ --cov-report xml

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build
