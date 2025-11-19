#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_message.sh

filter_by_invalid() (
    declare -r _expected="true"
    declare -r _invalid="$1"
    declare -r _message=$(constant::message_invalid)

    if [[ "${_invalid}" = "${_expected}" ]]; then
        shell::show_warning "${_message}"
    fi
)

filter_by_help() (
    declare -r _expected="true"
    declare -r _help="$1"
    declare -r _message_help=$(constant::help_help)

    if [[ "${_help}" = "${_expected}" ]]; then
        echo "${_message_help}"
        exit 1
    fi
)

filter_by_account() (
    declare -r _expected=$(constant::expected_name)
    declare -r _message=$(constant::message_user)

    declare -r user_name=$(whoami)

    if [[ "${user_name}" = "${_expected}" ]]; then
        shell::show_warning "${_message}"
    fi
)
