# Makefile for Django project

SHELL := /bin/bash

.ONESHELL:

# Define variables
.DEFAULT_GOAL := help


PORT = 8000
IP = localhost

LOCAL_SETTINGS = config.settings
SETTINGS = $(LOCAL_SETTINGS)

# Define the virtual environment name
VENV_NAME = .venv

PIPENV = pipenv
# Automatically get the project and app directories
PROJECT_DIR := $(shell dirname $(CURDIR))
APP_DIR := $(CURDIR)

# Ensure virtual environment is active before running any commands
PIPENV_SHELL = pipenv shell
PIPENV_RUN = pipenv run

PYTHON = python3
# Define manage.py command as $(MANAGE) for convenience
MANAGE = $(PIPENV_RUN) $(PYTHON) manage.py


# Default target when `make` is called without arguments
all:
	@echo "Running Server..."
	@gnome-terminal --tab --title="Server" --command="bash -c '$(PIPENV_SHELL); make runserver SETTINGS=$(SETTINGS); exec bash'" > /dev/null 2>&1
	@echo "Server & Celery running successfully."

dir:
	@echo "PROJECT_DIR: $(PROJECT_DIR)"
	@echo "APP_DIR: $(APP_DIR)"
	
# Activate virtual environment
venv:
	@gnome-terminal --tab --title="Virtual environment" --command="bash -c '$(PIPENV_SHELL); exec bash'" > /dev/null 2>&1
	@echo "Virtual environment running successfully."
	

collectstatic:  ## Collect static files
	$(MANAGE) collectstatic --noinput

# Run development server on localhost
runserver:
	$(MANAGE) runserver --settings=$(SETTINGS) $(IP):$(PORT)

# Create database tables and apply migrations
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Create a new app (replace `myapp` with your desired app name)
createapp:
	@read -p "Enter the name of the app: " app_name; \
	$(MANAGE) startapp $$app_name; \
	mv $$app_name $(APP_DIR)/apps/
	@echo "$$app_name app created successfully."

# Run tests
test:
	$(MANAGE) test

# Clean up unused files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete


# Help target to display available commands
help:
	@echo "Available commands:"
	@echo "  all            - Run project"
	@echo "  venv           - Activate virtual environment"
	@echo "  runserver      - Run development server on localhost."
	@echo "  migrate        - Apply migrations and create database tables."
	@echo "  createapp      - Create a new app (replace 'myapp' with your desired app name)."
	@echo "  test           - Run tests."
	@echo "  clean          - Clean up unused files."
	@echo "  collectstatic  - Collect static files."
