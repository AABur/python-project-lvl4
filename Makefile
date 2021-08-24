install: ## Install dependencies
	@poetry install

test: ## Run tests
	poetry run coverage run --source=page_loader -m pytest tests

lint: ## Run linter
	poetry run flake8 page_loader

selfcheck: ## Checks the validity of the pyproject.toml file
	poetry check

check: ## selfcheck + test + lint
	@make selfcheck
	@make test
	@make lint

build: ## Check and builds a package
	@make check
	@poetry build

package-install: ## build and install
	make build
	pip install dist/*.whl

run:
	poetry run python manage.py runserver

requirements:
	poetry export -f requirements.txt --output requirements.txt

cc-coverage: ## Prepare coverage report for Codeclimate
	poetry run coverage xml

help: ## This help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install test lint selfcheck check build package-install cc-coverage help requirements run
.DEFAULT_GOAL := help
