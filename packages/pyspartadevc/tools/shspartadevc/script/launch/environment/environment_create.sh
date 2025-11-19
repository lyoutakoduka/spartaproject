#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_export.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_status.sh

set_environment() (
    declare -r _quote="\""
    declare -r _expected="true"
    declare -r _key="$1"
    declare -r _value="$2"

    _create_environment() {
        declare -r quote_added=$(string_quoted "${_value}" "${_quote}")
        export_environment "${_key}" "${quote_added}"
    }

    _main() {
        declare -r status=$(get_status_environment "${_key}" "${_value}")

        if [[ "${status}" = "${_expected}" ]]; then
            _create_environment
        fi
    }

    _main
)
