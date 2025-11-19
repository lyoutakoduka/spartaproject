#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_name() (
    declare -r _empty=""
    declare -r _expected="true"
    declare -r _status="$1"
    declare -r _name_key=$(constant::name_key)

    _get_user_name() {
        if [[ "${_status}" != "${_expected}" ]]; then
            echo "${_empty}"
            return
        fi

        whoami
    }

    _main() {
        declare -r user_name=$(_get_user_name)
        set_environment "${_name_key}" "${user_name}"
    }

    _main
)
