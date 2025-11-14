#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/project/get_resource.sh

get_context_path() (
    declare -r _empty=""
    declare -r _file_path="forward.json"
    declare -r _filter=".forward"
    declare -r _executed_path="$1"
    declare -r _local_path="$2"

    _import_forward_link() {
        declare -r forward_path="$1"

        declare -r context_path=$(jq -r "${_filter}" "${forward_path}")
        echo "${context_path}"
    }

    _get_resource_root() {
        declare -r relative_path="$1"

        declare -r path=$(get_resource "${_executed_path}" "${relative_path}")
        echo "${path}"
    }

    _get_forward_link() {
        declare -r forward_path=$(_get_resource_root "${_file_path}")
        context_path=$(_import_forward_link "${forward_path}")

        echo "${context_path}"
    }

    _main() {
        declare path="${_empty}"

        if [[ -z "${_local_path}" ]]; then
            path=$(_get_forward_link)
        else
            path=$(_get_resource_root "${_local_path}")
        fi

        echo "${path}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
