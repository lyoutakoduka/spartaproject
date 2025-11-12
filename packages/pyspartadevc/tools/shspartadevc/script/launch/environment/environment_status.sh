#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_status_environment() (
    declare -r _key="$1"
    declare -r _value="$2"
    declare -r _empty=$(constant::empty)
    declare -r _success=$(constant::status_success)

    _main() {
        declare result="${_empty}"

        if [[ -n "${_key}" ]] && [[ -n "${_value}" ]]; then
            result="${_success}"
        fi

        echo "${result}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
