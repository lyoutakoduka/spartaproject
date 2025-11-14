#!/usr/bin/env bats

. packages/pyspartadevc/tests/shspartadevc/script/project/test_get_stack_trace.sh

_confirm_status() {
    declare -r _expected=0
    [[ "${status}" -eq "${_expected}" ]]
}

@test "test_get_stack_trace" {
    run test
    _confirm_status
}
