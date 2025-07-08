#!/bin/bash

if [ -z "$VIRTUAL_ENV_DIR" ]; then
  echo "Error: VIRTUAL_ENV_DIR environment variable is not set."
  exit 1
fi

project_name="md2mm"
venv_dir="$VIRTUAL_ENV_DIR/$project_name"

source "$venv_dir/bin/activate"
python main-ui.py
deactivate
