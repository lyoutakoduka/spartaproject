#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/string/string_assign.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

export_environment() (
    declare -r _command="export"
    declare -r _key="$1"
    declare -r _value="$2"

    declare -r export_pair=$(create_assign "${_key}" "${_value}")
    declare -r text="${_command} ${export_pair}"

    export_line "${text}"
)
