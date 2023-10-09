#!/usr/bin/env bash

export PYTHONPATH=${CWD}:${PYTHONPATH}

group=$1
interpreter="./poetry/linux/.venv/bin/"

execute_filter () {
    executable=$1
    argument=$2
    exec "$interpreter$executable" $argument
}

if [ "isort" = $group ]; then
    execute_filter "isort" "--check-only ."
elif [ "black" = $group ]; then
    execute_filter "black" "--check ."
elif [ "flake" = $group ]; then
    execute_filter "pflake8" "."
elif [ "pytest" = $group ]; then
    execute_filter "pytest" ""
fi
