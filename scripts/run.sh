#!/bin/bash

project_root="$(dirname ${PWD})"

python=python3 #"${project_root}/venv/bin/python"

run=${project_root}/src/main.py

data_file_path=${project_root}/data
data_file_name=state.json


# $python $run \
#     --data-file-path=${data_file_path} \
#     --data-file-name=${data_file_name}

$python $run

