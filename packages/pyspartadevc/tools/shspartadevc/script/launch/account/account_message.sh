#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh

show_identifier() (
    declare -r _status="$1"
    declare -r _expected="true"
    declare -r _identifier=$(constant::message_identifier)

    if [[ "${_status}" = "${_expected}" ]]; then
        show_log "${_identifier}"
    fi
)
