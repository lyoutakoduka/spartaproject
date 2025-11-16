#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh

test() (
    declare -r -i _offset=-1
    declare -r _group_path="path"
    declare -r _group_name="name"
    declare -r _expected_path="test_get_stack_trace.sh"
    declare -r _expected_name="_test_base_name"
    declare -r _expected_path_offset="get_stack_trace.sh"
    declare -r _expected_name_offset="get_selected_frame"

    _confirm_result() {
        declare -r result="$1"
        declare -r expected="$2"

        error_difference "${result}" "${expected}"
    }

    _test_base_path() {
        declare -r result=$(get_selected_frame "${_group_path}")
        declare -r parent_root=$(basename "${result}")

        _confirm_result "${parent_root}" "${_expected_path}"
    }

    _test_base_name() {
        declare -r result=$(get_selected_frame "${_group_name}")

        _confirm_result "${result}" "${_expected_name}"
    }

    _test_offset_path() {
        declare -r result=$(get_selected_frame "${_group_path}" "${_offset}")
        declare -r parent_root=$(basename "${result}")

        _confirm_result "${parent_root}" "${_expected_path_offset}"
    }

    _test_offset_name() {
        declare -r result=$(get_selected_frame "${_group_name}" "${_offset}")

        _confirm_result "${result}" "${_expected_name_offset}"
    }

    _main() {
        _test_base_path
        _test_base_name
        _test_offset_path
        _test_offset_name
    }

    _main
)

"$@"
