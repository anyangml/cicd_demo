help:
	@echo
	@echo "make <command>"
	@echo
	@echo "available commands:"
	@grep  "##"  $(MAKEFILE_LIST) | grep -v grep | column -t -s "##"
	@echo

.PHONY: init
init: ## install poetry and dependencies
	curl -sSL https://install.python-poetry.org | python - --version 1.2.2
	poetry install --sync

.PHONY: format
format: ## run code formatters
	poetry run python -m isort .isort.cfg .
	poetry run python -m flake8
	poetry run python -m black --line-length 130 .

.PHONY: test
test: ## run unit tests
	poetry run python -m pytest -vv

.PHONY: version
version: ## bump version
	bump2version setup.cfg --new-version $(new-version)
