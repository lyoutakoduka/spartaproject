#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_name() (
    declare -r _status="$1"
    declare -r _empty=$(constant::empty)
    declare -r _success=$(constant::status_success)
    declare -r _name_key=$(constant::name_key)

    _get_user_name() {
        declare user_name="${_empty}"

        if [[ "${_status}" = "${_success}" ]]; then
            user_name=$(whoami)
        fi

        echo "${user_name}"
    }

    _main() {
        declare -r user_name=$(_get_user_name)
        set_environment "${_name_key}" "${user_name}"
    }

    _main
)
