#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_user.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_identifier() (
    declare -r _status="$1"
    declare -r _user_key=$(constant::user_key)
    declare -r _empty=$(constant::empty)
    declare -r _success=$(constant::status_success)

    _get_user_value() {
        declare number="${_empty}"

        if [[ "${_status}" = "${_success}" ]]; then
            number=$(get_user_identifier)
        fi

        echo "${number}"
    }

    _main() {
        declare -r user_value=$(_get_user_value)
        set_environment "${_user_key}" "${user_value}"
    }

    _main
)
