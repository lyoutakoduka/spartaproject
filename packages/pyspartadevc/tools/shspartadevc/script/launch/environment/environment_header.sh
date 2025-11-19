#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

environment_comment() (
    declare -r _expected="true"
    declare -r _status="$1"
    declare -r _comment=$(constant::header_environment)

    if [[ "${_status}" = "${_expected}" ]]; then
        export_line "${_comment}"
    fi
)
