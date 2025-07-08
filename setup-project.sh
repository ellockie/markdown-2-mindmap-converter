#!/bin/bash

if [ -z "$VIRTUAL_ENV_DIR" ]; then
  echo "Error: VIRTUAL_ENV_DIR environment variable is not set."
  exit 1
fi


# PYENV environment

# Specify Python version
python_version="3.12.6"
# Check if Python version is installed
if ! pyenv versions | grep -q "$python_version"; then
    echo "Error: Python $python_version is not installed. Please install it using pyenv."
    exit 1
fi
pyenv local $python_version # set the python version for the project
python -m venv "$venv_dir"  # venv will use the specified version


project_name="md2mm"
venv_dir="$VIRTUAL_ENV_DIR/$project_name"

if [ -d "$venv_dir" ]; then
  echo "Virtual environment already exists: $venv_dir"
else
  python3 -m venv "$venv_dir"
  echo "Virtual environment created: $venv_dir"

  # Install dependencies (optional - you can do this later)
  source "$venv_dir/bin/activate"
  pip install -r requirements.txt
  deactivate
fi
