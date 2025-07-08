#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# This is a command built into bash and some other shells that automatically export any subsequently defined variables to the environment of child processes. Here, -a is a flag that stands for "allexport".
# set -a

cd /Users/lpi23/Dropbox/___Goals_Projects___

export PYTHONPATH="$PYTHONPATH:$PWD"

# source is a bash shell built-in command that executes the content of the file passed as argument, in the current shell. .env is commonly used to hold a list of environment variables to be used by an application, with each line in the file being a key value pair in the form KEY=VALUE.
# The source .env command reads the file named .env in the current directory and executes the commands in the current shell environment. Because set -a was called earlier, all variables defined in the .env file will be exported as environment variables, not just defined as shell variables.
source ~/_VENVS/gole/bin/activate
