#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_context_path.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh

test() (
    declare -r _status=1
    declare -r _group="path"
    declare -r _local_path="context.json"
    declare -r _root_main="packages/pyspartadevc/tests/shspartadevc"
    declare -r _root_sub="script/project/resource/context.json"

    _get_context_path() {
        echo "${_root_main}/${_root_sub}"
    }

    _confirm_result() {
        declare -r result="$1"

        declare -r context_path=$(_get_context_path)

        error_difference "${result}" "${context_path}" || exit "${_status}"
    }

    _get_executed_path() {
        declare -r executed=$(get_selected_frame "${_group}")
        echo "${executed}"
    }

    _test_base() {
        declare -r executed=$(_get_executed_path)
        declare -r result=$(get_context_path "${executed}" "${_local_path}")

        _confirm_result "${result}"
    }

    _test_forward() {
        declare -r executed=$(_get_executed_path)
        declare -r result=$(get_context_path "${executed}")

        _confirm_result "${result}"
    }

    _main() {
        _test_base
        _test_forward
    }

    _main
)

"$@"
