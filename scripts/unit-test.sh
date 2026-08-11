#!/bin/bash

project_root="$(dirname ${PWD})"

python=python3 #"${project_root}/venv/bin/python"

tests=tests

pushd ${project_root}

$python -m unittest discover -s $tests -v

popd
