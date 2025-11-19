#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

#*  Args:
#*      $1 (string):
#*          Command to export environment variable will be added to file.
#*
set_group_identifier() (
    declare -r _empty=""
    declare -r _expected="true"
    declare -r _status="$1"
    declare -r _identifier_key=$(constant::group_key)

    _get_identifier() {
        if [[ "${_status}" != "${_expected}" ]]; then
            echo "${_empty}"
            return
        fi

        id --group
    }

    _main() {
        declare -r identifier=$(_get_identifier)
        set_environment "${_identifier_key}" "${identifier}"
    }

    _main
)
