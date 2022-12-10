install: ## install dependencies
	@poetry install

test: ## run tests
	poetry run coverage run --source=task_manager -m pytest tests

cc-coverage: ## Prepare coverage report for Codeclimate
	poetry run coverage xml

lint: ## run linter
	poetry run flake8 task_manager/

selfcheck: ## check pyproject.toml
	poetry check

check: ## selfcheck + test + lint
	@make selfcheck
	@make test
	@make lint

run: ## run local server
	poetry run python manage.py runserver

open: ## open local server
	open http://127.0.0.1:8000/

migrate: ## django migrate
	poetry run python manage.py migrate

migrations: ## django makemigrations
	poetry run python manage.py makemigrations

createsuperuser: ## createsuperuser
	poetry run python manage.py createsuperuser

setup: ## initial setup
	make install
	make migrate
	make createsuperuser

clean: ## clean up python cache files
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

locale-update: ## update locale files
	poetry run django-admin makemessages --locale ru

locale-compile: ## compile locale files
	poetry run django-admin compilemessages --locale ru

help: ## this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# .PHONY: install test lint selfcheck check build package-install cc-coverage help init setup
.DEFAULT_GOAL := help
