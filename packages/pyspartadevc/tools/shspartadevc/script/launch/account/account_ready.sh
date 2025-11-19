#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_group.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_header.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_name.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_user.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

ready_identifier() (
    declare -r _success="true"
    declare -r _fail="false"
    declare -r -i _expected=$(constant::expected_identifier)

    _set_user_information() {
        declare -r status="$1"

        show_identifier "${status}"
        environment_comment "${status}"
        set_user_name "${status}"
        set_user_identifier "${status}"
        set_group_identifier "${status}"
    }

    _get_status_identifier() {
        declare -r identifier=$(id --user)

        if [[ "${identifier}" -ne "${_expected}" ]]; then
            echo "${_success}"
        else
            echo "${_fail}"
        fi
    }

    _main() {
        declare -r status=$(_get_status_identifier)
        _set_user_information "${status}"
    }

    _main
)
