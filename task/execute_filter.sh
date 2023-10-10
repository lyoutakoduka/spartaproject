#!/usr/bin/env bash

export PYTHONPATH=${CWD}:${PYTHONPATH}

filter_group=$1
execute_target="."
interpreter="./poetry/linux/.venv/bin/"

execute_filter () {
    executable=$1
    argument=$2
    exec "$interpreter$executable" $argument
}

if [ "isort" = $filter_group ]; then
    execute_filter "isort" "--check-only $execute_target"
elif [ "black" = $filter_group ]; then
    execute_filter "black" "--check $execute_target"
elif [ "flake" = $filter_group ]; then
    execute_filter "pflake8" $execute_target
elif [ "pytest" = $filter_group ]; then
    execute_filter "pytest" $execute_target
fi
