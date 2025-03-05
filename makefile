# .PHONY: psql up down venv check-deps update-deps install-deps isort black mypy flake8 bandit lint test migrate serve

# ifneq (,$(wildcard ./.env))
#     include .env
#     export
# endif

# VENV=.venv
# PYTHON=$(VENV)/bin/python3

# cmd-exists-%:
# 	@hash $(*) > /dev/null 2>&1 || \
# 		(echo "ERROR: '$(*)' must be installed and available on your PATH."; exit 1)

# psql: cmd-exists-psql
# 	psql "${DATABASE_URL}"

up:  ## Run Docker Compose services
	docker-compose -f docker-compose.yml up db -d

# down:  ## Shutdown Docker Compose services
# 	docker-compose -f docker-compose.local.yml down

# venv: requirements-dev.txt Makefile
# 	python3 -m pip install --upgrade pip setuptools wheel
# 	python3 -m venv $(VENV)
# 	$(PYTHON) -m pip install -r requirements-dev.txt

# check-deps:  ## Check new versions and update deps
# 	$(PYTHON) -m pur -r requirements-dev.txt -d

# update-deps:  ## Check new versions and update deps
# 	$(PYTHON) -m pur -r requirements-dev.txt

install-deps:  ## Install dependencies
	python -m pip install -r requirements.txt

# isort:
# 	$(PYTHON) -m isort --check-only .

black:
	python -m black --check .

# mypy:
# 	$(PYTHON) -m mypy .

# flake8:
# 	$(PYTHON) -m flake8 .

bandit:
	python -m bandit -r main

# lint: isort black mypy flake8 bandit

.PHONY: test

test:  ## Run tests
	export PY_ENV=test
	python -m pytest


.PHONY: migrate-up migrate-down migration-status migration-current

migrate-up:  ## Apply latest alembic migrations
	python -m alembic upgrade head

migrate-down:  ## Downgrade alembic migrations
	python -m alembic downgrade -1

migration-status:  ## Show current alembic migration
	python -m alembic history

migration-current:
	python -m alembic current



.PHONY: serve-dev
# serve:  ## Run application server in prod
# 	uvicorn main:app --host 0.0.0.0 --port 8000:8000

.PHONY: serve
serve:  ## Run application server in prod
	python -m main.py


.PHONY: serve-dev
serve-dev:  ## Run application server in development
	export PY_ENV=development
	export DEBUG=True
	python main.py
