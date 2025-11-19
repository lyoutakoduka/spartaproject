#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_error.sh

#*  Filter the processing by invalid arguments.
#*
#*  Args:
#*      _invalid (string): Set "true" if invalid arguments are found.
#*
#*  Error:
#*      _show_and_exit (function): exit 1
#*
filter_by_invalid() (
    declare -r _invalid="$1"
    declare -r _success="true"
    declare -r _message=$(constant::message_invalid)

    _show_and_exit() {
        show_error "${_message}"
        exit 1
    }

    _main() {
        if [[ "${_invalid}" = "${_success}" ]]; then
            _show_and_exit
        fi
    }

    _main
)
