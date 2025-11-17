#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/constant/constant_filter.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh
. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/constant/constant_import.sh

test_filter() (
    declare -r _group="path"
    declare -r _filter_trim="\n "
    declare -r _filter_main="fruits"
    declare -r _filter_sub="red"
    declare -r _expected="apple"

    _test_get_frame_path() (
        declare -r executed=$(get_selected_frame "${_group}")
        echo "${executed}"
    )

    _filter_constant() {
        declare text_json="$1"

        text_json=$(filter_constant "${text_json}" "${_filter_main}")
        text_json=$(filter_constant "${text_json}" "${_filter_sub}")

        echo "${text_json}"
    }

    _main() {
        declare -r executed=$(_test_get_frame_path)
        declare -r text_json=$(import_constant "${executed}" "${_filter_trim}")
        declare -r result=$(_filter_constant "${text_json}")

        shell::error_difference "${result}" "${_expected}"
    }

    _main
)

"$@"
