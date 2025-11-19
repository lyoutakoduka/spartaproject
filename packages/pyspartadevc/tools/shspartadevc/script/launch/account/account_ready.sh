#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/variable/variable_group.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_header.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/variable/variable_name.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/variable/variable_user.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

ready_identifier() (
    declare -r -i _expected=$(constant::expected_identifier)

    _set_user_information() {
        declare -r status="true"

        show_identifier "${status}"
        environment_comment "${status}"
        set_user_name "${status}"
        set_user_identifier "${status}"
        set_group_identifier "${status}"
    }

    _main() {
        declare -r identifier=$(id --user)

        if [[ "${identifier}" -ne "${_expected}" ]]; then
            _set_user_information
        fi
    }

    _main
)
