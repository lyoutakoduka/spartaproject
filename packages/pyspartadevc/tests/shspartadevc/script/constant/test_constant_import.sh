#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/constant/constant_import.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh
. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

test_import() (
    declare -r _group="path"
    declare -r _trim_filter="\n "
    declare -r _expected='{"fruits":{"red":"apple"}}'

    _main() {
        declare -r executed=$(get_selected_frame "${_group}")
        declare -r result=$(import_constant "${executed}" "${_trim_filter}")

        shell::error_difference "${result}" "${_expected}"
    }

    _main
)

"$@"
