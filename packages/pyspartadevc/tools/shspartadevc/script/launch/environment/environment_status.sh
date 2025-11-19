#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_status_environment() (
    declare -r _empty=""
    declare -r _success="true"
    declare -r _key="$1"
    declare -r _value="$2"

    if [[ -n "${_key}" ]] && [[ -n "${_value}" ]]; then
        echo "${_success}"
        return
    fi

    echo "${_empty}"
)
