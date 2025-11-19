#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_message.sh
filter_by_account() (
    declare -r _expected=$(constant::expected_name)
    declare -r _message=$(constant::message_user)

    declare -r user_name=$(whoami)

    if [[ "${user_name}" = "${_expected}" ]]; then
        shell::show_warning "${_message}"
    fi
)
