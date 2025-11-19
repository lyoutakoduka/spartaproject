#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_identifier() (
    declare -r _empty=""
    declare -r _expected="true"
    declare -r _status="$1"
    declare -r _user_key=$(constant::user_key)

    _get_user_value() {
        if [[ "${_status}" != "${_expected}" ]]; then
            echo "${_empty}"
            return
        fi
        id --user
    }

    _main() {
        declare -r user_value=$(_get_user_value)
        set_environment "${_user_key}" "${user_value}"
    }

    _main
)
