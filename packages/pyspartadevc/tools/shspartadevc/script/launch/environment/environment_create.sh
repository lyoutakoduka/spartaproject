#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_export.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_status.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/string/string_quote.sh

set_environment() (
    declare -r _key="$1"
    declare -r _value="$2"
    declare -r _success=$(constant::status_success)

    _create_environment() {
        declare -r quote_added=$(add_double_quote "${_value}")
        export_environment "${_key}" "${quote_added}"
    }

    _get_status() {
        declare -r status=$(get_status_environment "${_key}" "${_value}")
        echo "${status}"
    }

    _main() {
        declare -r status=$(_get_status)

        if [[ "${status}" = "${_success}" ]]; then
            _create_environment
        fi
    }

    _main
)
