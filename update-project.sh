#!/bin/bash

if [ -z "$VIRTUAL_ENV_DIR" ]; then
  echo "Error: VIRTUAL_ENV_DIR environment variable is not set."
  exit 1
fi

project_name="md2mm"
venv_dir="$VIRTUAL_ENV_DIR/$project_name"

if [ -d "$venv_dir" ]; then
  source "$venv_dir/bin/activate"
  pip install -r requirements.txt
  deactivate
else
  echo "Virtual environment not found. Run setup_project.sh first."
fi
