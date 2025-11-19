#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_status.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

set_environment() (
    declare -r _quote="\""
    declare -r _command="export"
    declare -r _key="$1"
    declare -r _value="$2"

    _create_environment() {
        declare -r quote_added=$(string_quoted "${_value}" "${_quote}")
        export_lines "${_command} ${_key}=${quote_added}"
    }

    _main() {
        if [[ -n "${_key}" ]] && [[ -n "${_value}" ]]; then
            _create_environment
        fi
    }

    _main
)
