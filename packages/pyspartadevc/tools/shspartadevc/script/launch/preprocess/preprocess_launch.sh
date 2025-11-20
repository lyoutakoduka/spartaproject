#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_script.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show_message.sh

_select_arguments() (
    declare -r _success="true"
    declare -r _fail="false"

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

_handling_arguments() (
    declare -r _separator=","
    declare -r _expected="true"
    declare -r _arguments=("$@")
    declare -r _message_invalid=$(constant::message_invalid)
    declare -r _message_help=$(constant::help_help)

    _filter_by_invalid() (
        declare -r _invalid="$1"

        if [[ "${_invalid}" = "${_expected}" ]]; then
            shell::show_warning "${_message_invalid}"
        fi
    )

    _filter_by_help() (
        declare -r _help="$1"

        if [[ "${_help}" = "${_expected}" ]]; then
            echo "${_message_help}"
            exit 1
        fi
    )

    _filter_by_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        _filter_by_invalid "${invalid}" || exit 1
        _filter_by_help "${help}" || exit 1
    }

    _main() {
        declare -r flags=$(_select_arguments "${_arguments[@]}")

        declare help invalid
        IFS="${_separator}" read -r help invalid <<<"${flags}"

        _filter_by_arguments "${help}" "${invalid}"
    }

    _main
)

preprocess_launch() (
    declare -r _create="create"
    declare -r _attach="attach"
    declare -r _arguments=("$@")
    declare -r _expected=$(constant::expected_name)
    declare -r _message=$(constant::message_user)

    _filter_by_account() (
        declare -r user_name=$(whoami)

        if [[ "${user_name}" = "${_expected}" ]]; then
            shell::show_warning "${_message}"
        fi
    )

    _main() {
        _handling_arguments "${_arguments[@]}" || exit 1
        _filter_by_account || exit 1

        create_preprocess_script "${_create}"
        create_preprocess_script "${_attach}"
    }

    _main
)
