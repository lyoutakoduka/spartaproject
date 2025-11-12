#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_group.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_group_identifier() (
    declare -r _status="$1"
    declare -r _empty=$(constant::empty)
    declare -r _success=$(constant::status_success)
    declare -r _identifier_key=$(constant::group_key)

    _get_identifier() {
        declare identifier="${_empty}"

        if [[ "${_status}" = "${_success}" ]]; then
            identifier=$(get_group_identifier)
        fi

        echo "${identifier}"
    }

    _main() {
        declare -r identifier=$(_get_identifier)
        set_environment "${_identifier_key}" "${identifier}"
    }

    _main
)
