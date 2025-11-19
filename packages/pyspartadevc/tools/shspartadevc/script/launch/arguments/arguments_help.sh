#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

filter_by_help() (
    declare -r _expected="true"
    declare -r _help="$1"
    declare -r _message_help=$(constant::help_help)

    if [[ "${_help}" = "${_expected}" ]]; then
        echo "${_message_help}"
        exit 1
    fi
)
