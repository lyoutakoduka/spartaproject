#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/string/string_assign.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

export_environment() (
    declare -r _key="$1"
    declare -r _value="$2"
    declare -r _command=$(constant::environment)

    _get_export_text() {
        declare -r command_export="$1"
        declare -r export_pair="$2"

        echo "${command_export} ${export_pair}"
    }

    _get_command_text() {
        declare -r export_pair=$(create_assign "${_key}" "${_value}")
        declare -r text=$(_get_export_text "${_command}" "${export_pair}")

        echo "${text}"
    }

    _main() {
        declare -r text=$(_get_command_text)
        export_line "${text}"
    }

    _main
)
