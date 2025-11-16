#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

filter_by_help() (
    declare -r _help="$1"
    declare -r _message="$2"
    declare -r _empty=$(constant::empty)
    declare -r _indent=$(constant::indent)
    declare -r _success=$(constant::status_success)
    declare -r _message_header=$(constant::help_header)
    declare -r _message_help=$(constant::help_help)

    _show_arguments() {
        declare text
        for text in "$@"; do
            echo "${text}"
        done
    }

    _get_message_section() {
        echo "${_indent}${_message}"
    }

    _get_arguments() {
        declare -r message_section=$(_get_message_section)

        _show_arguments \
            "${_message_header}" \
            "${message_section}" \
            "${_empty}" \
            "${_message_help}"
    }

    _show_and_exit() {
        _get_arguments
        exit 1
    }

    _main() {
        if [[ "${_help}" = "${_success}" ]]; then
            _show_and_exit
        fi
    }

    _main
)
