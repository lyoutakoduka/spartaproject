#!/usr/bin/env bash

export PYTHONPATH=${CWD}:${PYTHONPATH}

filter_group=$1
interpreter="./poetry/linux/.venv/bin/"

execute_filter () {
    executable=$1
    argument=$2
    exec "$interpreter$executable" $argument
}

if [ "isort" = $filter_group ]; then
    execute_filter "isort" "--check-only ."
elif [ "black" = $filter_group ]; then
    execute_filter "black" "--check ."
elif [ "flake" = $filter_group ]; then
    execute_filter "pflake8" "."
elif [ "pytest" = $filter_group ]; then
    execute_filter "pytest" ""
fi
