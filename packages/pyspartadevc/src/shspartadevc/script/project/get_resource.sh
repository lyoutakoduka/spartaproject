#!/bin/bash

get_resource() (
    declare -r _resource_name="resource"
    declare -r _executed_path="$1"
    declare -r _local_path="$2"

    _get_resource_root() {
        declare -r parent_root=$(dirname "${_executed_path}")
        echo "${parent_root}/${_resource_name}"
    }

    _main() {
        declare -r resource_root=$(_get_resource_root)

        if [[ -z "${_local_path}" ]]; then
            echo "${resource_root}"
        else
            echo "${resource_root}/${_local_path}"
        fi
    }

    declare -r result=$(_main)
    echo "${result}"
)
