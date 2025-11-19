#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_error.sh

filter_by_account() (
    declare -r _expected="root"
    declare -r _message=$(constant::message_user)

    _show_and_exit() {
        show_error "${_message}"
        exit 1
    }

    _main() {
        declare -r user_name=$(whoami)

        if [[ "${user_name}" = "${_expected}" ]]; then
            _show_and_exit
        fi
    }

    _main
)
