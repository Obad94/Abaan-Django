# Makefile for Django project

SHELL := /bin/bash

.ONESHELL:

# Define variables
.DEFAULT_GOAL := help

COLOR_RESET := $(shell tput sgr0)
COLOR_RED := $(shell tput setaf 1)
COLOR_YELLOW := $(shell tput setaf 3)
COLOR_GREEN := $(shell tput setaf 2)
COLOR_MAGENTA := $(shell tput setaf 5)
COLOR_CYAN := $(shell tput setaf 6)

PORT = 8000
IP = localhost

LOCAL_SETTINGS = config.settings
SETTINGS = $(LOCAL_SETTINGS)

# Define the virtual environment name
VENV_NAME = .venv

PIPENVIRON = pipenv
# Automatically get the project and app directories
PROJECT_DIR := $(shell dirname $(CURDIR))
APP_DIR := $(CURDIR)

PROJECT_NAME := $(shell basename "$(APP_DIR)")

# Ensure virtual environment is active before running any commands
PIPENV_SHELL = pipenv shell
PIPENV_RUN = pipenv run

PYTHON ?= python3
PIP ?= pip3
# Define manage.py command as $(MANAGE) for convenience
MANAGE = $(PIPENV_RUN) $(PYTHON) manage.py

SCRIPTS_DIR := config/scripts

export PYTHON_PATH := $(shell which $(PYTHON) 2>/dev/null)
export PIP_PATH := $(shell which $(PIP) 2>/dev/null)
export PIPENV := $(shell which $(PIPENVIRON) 2> /dev/null)

# Default target when `make` is called without arguments
all:
	@gnome-terminal --tab --title="Server" --command="bash -c 'make runserver SETTINGS=$(SETTINGS); exec bash'" > /dev/null 2>&1
	printf "$(COLOR_GREEN)[Success]: Server running successfully. $(COLOR_RESET)\n"	

dir-path-name:
	@printf "PROJECT_DIR: $(PROJECT_DIR)  \n"
	@printf "APP_DIR: $(APP_DIR)  \n"
	@printf "PROJECT_NAME: $(PROJECT_NAME)  \n"
	
# Activate virtual environment
venv:
	@gnome-terminal --tab --title="Virtual environment" --command="bash -c '$(PIPENV_SHELL); exec bash'" > /dev/null 2>&1
	printf "$(COLOR_GREEN)[Success]: Virtual environment running successfully. $(COLOR_RESET)\n"	

collectstatic:  ## Collect static files
	$(MANAGE) collectstatic --noinput

# Run development server on localhost
runserver:
	@$(MANAGE) runserver --settings=$(SETTINGS) $(IP):$(PORT) 

# Create database tables and apply migrations
migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

# Create a new app (replace `myapp` with your desired app name)
createapp:
	@read -p "Enter the name of the app: " app_name; \
	$(MANAGE) startapp $$app_name; \
	mv $$app_name $(APP_DIR)/apps/ 
	@printf "$(COLOR_GREEN)[Success]: $$app_name app created successfully.$(COLOR_RESET)\n"
	$(PYTHON) $(SCRIPTS_DIR)/add_to_installed_apps.py $$app_name
	$(PYTHON) $(SCRIPTS_DIR)/edit_apps.py $(APP_DIR)/apps/$$app_name $$app_name; \

# Run tests
test:
	$(MANAGE) test

# Clean up unused files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

check-python-pip:
	@printf "$(COLOR_CYAN)[Info]: Checking for $(PYTHON) and $(PIP)...$(COLOR_RESET)\n"; \
	if [ -z "$(PYTHON_PATH)" ]; then \
		printf "$(COLOR_RED)[Error]: $(PYTHON) is not installed. Please install $(PYTHON) first.$(COLOR_RESET)\n"; \
	else \
		printf "$(COLOR_GREEN)[Success]: Found $(PYTHON) at $(PYTHON_PATH): $(COLOR_RESET)"; \
		$(PYTHON_PATH) --version; \
	fi; \
	if [ -z "$(PIP_PATH)" ]; then \
		printf "$(COLOR_RED)[Error]: $(PIP) is not installed. Please install $(PIP) first.$(COLOR_RESET)\n"; \
	else \
		printf "$(COLOR_GREEN)[Success]: Found $(PIP) at $(PIP_PATH): $(COLOR_RESET)"; \
		$(PIP_PATH) --version; \
	fi

install-pipenv:
	@if [ -z "$$PIP_PATH" ]; then \
		exit 1; \
	fi
	$$PIP_PATH install pipenv

install-dependencies: 
	export PIPENV_VENV_IN_PROJECT=1
	pipenv install

setup: check-python-pip install-pipenv install-dependencies


uninstall-dep:
	@read -p "Are you sure you want to uninstall all dependencies? (Y/n) " confirm; \
	if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
		$$PIP_PATH uninstall pipenv
	else \
		printf "$(COLOR_YELLOW)[Warning]: Uninstall cancelled.$(COLOR_RESET)\n"
	fi

rename:
	@read -p "Enter the new project name: " new_name; \
	if [ -z "$$new_name" ]; then \
		printf "$(COLOR_RED)[Error]: Project name cannot be empty.$(COLOR_RESET)\n"
	else \
		printf "$(COLOR_CYAN)[Info]: Renaming the project name will result in the deletion of the current Virtual Environment.$(COLOR_RESET)\n"
		printf "$(COLOR_CYAN)[Info]: This is necessary to ensure that the new project name is selected correctly in the virtual environment.$(COLOR_RESET)\n"
		printf "$(COLOR_CYAN)[Info]: A new Virtual Environment will be installed with the updated project name.$(COLOR_RESET)\n"
		printf "Are you sure you want to continue? (Y/n) : "
		read -r confirm; \
		if [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]; then \
			rm -rf .venv
			sed -i 's/PROJECT_NAME := $(PROJECT_NAME)/PROJECT_NAME := $$new_name/g' Makefile; \
			# Rename the project directory
			mv $(PROJECT_DIR)/$(PROJECT_NAME) $(PROJECT_DIR)/$$new_name; \
			rm -rf $(APP_DIR)
			printf "$(COLOR_GREEN)[Success]: Project successfully renamed to $$new_name...$(COLOR_RESET)\n"
			cd $(PROJECT_DIR)/$$new_name; \
			printf "$(COLOR_YELLOW)[Warning]: You are still in the old directory, kindly change your directory to $(PROJECT_DIR)/$$new_name.$(COLOR_RESET)\n"
			gnome-terminal --working-directory=$(PROJECT_DIR)/$$new_name -- bash -c "make setup && make all"; \
		else \
			printf "$(COLOR_YELLOW)[Warning]: Project renaming has been cancelled.$(COLOR_RESET)\n"
		fi \
	fi

# Help target to display available commands
help:
	@printf "$(COLOR_MAGENTA)# Available commands:$(COLOR_RESET)\n"
	@printf "$(COLOR_GREEN)  - all                $(COLOR_RESET) Run the project.\n"
	@printf "$(COLOR_GREEN)  - venv               $(COLOR_RESET) Activate the virtual environment.\n"
	@printf "$(COLOR_GREEN)  - runserver          $(COLOR_RESET) Run the development server on localhost.\n"
	@printf "$(COLOR_GREEN)  - migrate            $(COLOR_RESET) Apply migrations and create database tables.\n"
	@printf "$(COLOR_GREEN)  - createapp          $(COLOR_RESET) Create a new app.\n"
	@printf "$(COLOR_GREEN)  - test               $(COLOR_RESET) Run tests.\n"
	@printf "$(COLOR_GREEN)  - clean              $(COLOR_RESET) Clean up cache files.\n"
	@printf "$(COLOR_GREEN)  - collectstatic      $(COLOR_RESET) Collect static files.\n"
	@printf "$(COLOR_GREEN)  - rename             $(COLOR_RESET) Rename the project.\n"
	@printf "$(COLOR_GREEN)  - setup              $(COLOR_RESET) Setup the project.\n"
	@printf "$(COLOR_GREEN)  - uninstall-dep      $(COLOR_RESET) Uninstall project dependencies.\n"
	@printf "$(COLOR_GREEN)  - check-python-pip   $(COLOR_RESET) Check for Python and pip installations.\n"
	@printf "$(COLOR_GREEN)  - dir-path-name      $(COLOR_RESET) Print directory path, and project name.\n"