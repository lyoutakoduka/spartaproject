#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/project/get_context_path.sh

#*  Args:
#*      $1 (string): The file path of the calling script.
#*
#*      $2 (string): Filter string used to trim the imported json text.
#*
#*  Return:
#*      (string) Filtered or raw json text you imported.
#*
import_constant() (
    declare -r _executed="$1"
    declare -r _trim_filter="$2"

    _get_context_path() {
        declare -r context_path=$(get_context_path "${_executed}")
        echo "${context_path}"
    }

    _filter_text() {
        declare -r text_json="$1"

        declare -r filtered=$(echo "${text_json}" | tr -d "${_trim_filter}")
        echo "${filtered}"
    }

    _main() {
        declare -r context_path=$(_get_context_path)
        declare -r text_json=$(cat "${context_path}")
        declare -r result=$(_filter_text "${text_json}")

        echo "${result}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
