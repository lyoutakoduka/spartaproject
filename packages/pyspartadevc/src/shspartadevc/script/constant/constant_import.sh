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

    _filter_text() {
        declare -r text_json="$1"
        echo "${text_json}" | tr -d "${_trim_filter}"
    }

    _main() {
        declare -r context_path=$(get_context_path "${_executed}")
        declare -r text_json=$(cat "${context_path}")
        _filter_text "${text_json}"
    }

    _main
)
