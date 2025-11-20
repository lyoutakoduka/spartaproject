#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_context_path.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh

_confirm_result() (
    declare -r result="$1"
    declare -r _root_main="packages/pyspartadevc/tests/shspartadevc"
    declare -r _root_sub="script/project/resource/context.json"

    shell::error_difference "${result}" "${_root_main}/${_root_sub}"
)

_get_executed_path() (
    declare -r _group="path"
    get_selected_frame "${_group}"
)

test_base() (
    declare -r _local_path="context.json"

    declare -r _executed=$(_get_executed_path)
    declare -r _result=$(get_context_path "${_executed}" "${_local_path}")

    _confirm_result "${_result}" || exit 1
)

test_forward() (
    declare -r _executed=$(_get_executed_path)
    declare -r _result=$(get_context_path "${_executed}")

    _confirm_result "${_result}" || exit 1
)

"$@"
