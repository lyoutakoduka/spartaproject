#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_error.sh

filter_by_invalid() (
    declare -r _expected="true"
    declare -r _invalid="$1"
    declare -r _message=$(constant::message_invalid)

    if [[ "${_invalid}" = "${_expected}" ]]; then
        show_error "${_message}"
        exit 1
    fi
)
