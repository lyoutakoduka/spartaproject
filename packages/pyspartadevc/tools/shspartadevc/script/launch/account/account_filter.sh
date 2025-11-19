#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_error.sh

filter_by_account() (
    declare -r _expected=$(constant::root)
    declare -r _message=$(constant::message_user)

    _main() {
        declare -r user_name=$(whoami)

        if [[ "${user_name}" = "${_expected}" ]]; then
            show_error "${_message}"
            exit 1
        fi
    }

    _main
)
