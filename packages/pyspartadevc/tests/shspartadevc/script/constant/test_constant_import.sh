#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/constant/constant_import.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh
. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

_test_get_frame_path() (
    declare -r _group="path"

    declare -r executed=$(get_selected_frame "${_group}")
    echo "${executed}"
)

test_print() (
    declare -r _expected_array=(
        '{'
        '  "fruits": {'
        '    "red": "apple"'
        '  }'
        '}'
    )

    _get_expected() {
        for item in "${_expected_array[@]}"; do
            echo "${item}"
        done
    }

    _main() {
        declare -r executed=$(_test_get_frame_path)
        declare -r result=$(import_constant "${executed}")
        declare -r _expected=$(_get_expected)

        shell::error_difference "${result}" "${_expected}"
    }

    _main
)

test_import() (
    declare -r _trim_filter="\n "
    declare -r _expected='{"fruits":{"red":"apple"}}'

    _main() {
        declare -r executed=$(_test_get_frame_path)
        declare -r result=$(import_constant "${executed}" "${_trim_filter}")

        shell::error_difference "${result}" "${_expected}"
    }

    _main
)

"$@"
