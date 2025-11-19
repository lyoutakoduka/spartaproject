#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

select_arguments() (
    declare -r _success="true"
    declare -r _fail="false"
    declare -r _separator=","

    _shift_arguments() {
        shift $((OPTIND - 1))
    }

    _merge_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        echo "${help}${_separator}${invalid}"
    }

    _main() {
        declare help="${_fail}"
        declare invalid="${_fail}"

        declare opt
        while getopts "h" opt; do
            case "${opt}" in
            h)
                help="${_success}"
                ;;
            \?)
                invalid="${_success}"
                ;;
            *) ;;
            esac
        done

        _shift_arguments

        declare -r merged=$(_merge_arguments "${help}" "${invalid}")
        echo "${merged}"
    }

    declare -r result=$(_main "$@")
    echo "${result}"
)
