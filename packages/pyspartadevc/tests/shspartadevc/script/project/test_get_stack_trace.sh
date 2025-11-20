#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh

test_base_path() (
    declare -r _group="path"
    declare -r _expected="test_get_stack_trace.sh"

    declare -r _result=$(get_selected_frame "${_group}")
    declare -r _parent_root=$(basename "${_result}")

    shell::error_difference "${_parent_root}" "${_expected}"
)

test_base_name() (
    declare -r _group="name"
    declare -r _expected="test_base_name"

    declare -r _result=$(get_selected_frame "${_group}")

    shell::error_difference "${_result}" "${_expected}"
)

test_offset_path() (
    declare -r _group="path"
    declare -r _expected="get_stack_trace.sh"
    declare -r -i _offset=-1

    declare -r _result=$(get_selected_frame "${_group}" "${_offset}")
    declare -r _parent_root=$(basename "${_result}")

    shell::error_difference "${_parent_root}" "${_expected}"
)

test_offset_name() (
    declare -r _group="name"
    declare -r _expected="get_selected_frame"
    declare -r -i _offset=-1

    declare -r _result=$(get_selected_frame "${_group}" "${_offset}")

    shell::error_difference "${_result}" "${_expected}"
)

"$@"
