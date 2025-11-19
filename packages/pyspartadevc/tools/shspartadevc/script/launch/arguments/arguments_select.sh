#!/bin/bash

select_arguments() (
    declare -r _success="true"
    declare -r _fail="false"
    declare -r _separator=","

    _shift_arguments() {
        shift $((OPTIND - 1))
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

        echo "${help},${invalid}"
    }

    _main "$@"
)
