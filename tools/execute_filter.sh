#!/usr/bin/env bash

export PYTHONPATH=${CWD}:${PYTHONPATH}

filter_group=$1
execute_target=$2
interpreter="./poetry/linux/.venv/bin/"

if [[ -z "$execute_target" ]]; then
    execute_target="."
fi

execute_filter () {
    executable=$1
    argument=$2
    exec "$interpreter$executable" $argument
}

if [ "mypy" = $filter_group ]; then
    execute_filter "mypy" $execute_target
elif [ "pytest" = $filter_group ]; then
    execute_filter "pytest" $execute_target
fi
