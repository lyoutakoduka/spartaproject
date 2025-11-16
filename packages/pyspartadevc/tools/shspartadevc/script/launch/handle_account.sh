#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_account.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_error.sh

#*  Filter the processing by user name.
#*
#*  Error:
#*    _show_and_exit (function): exit 1
#*
filter_by_account() (
    declare -r _expected=$(constant::root)
    declare -r _message=$(constant::message_user)

    _show_and_exit() {
        show_error "${_message}"
        exit 1
    }

    _main() {
        declare -r user_name=$(get_user_name)

        if [[ "${user_name}" = "${_expected}" ]]; then
            _show_and_exit
        fi
    }

    _main
)
