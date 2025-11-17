#!/usr/bin/env bats

. packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
. packages/pyspartadevc/tests/shspartadevc/script/project/test_get_stack_trace.sh

_confirm_status() {
    declare -r _expected=0
    [[ "${status}" -eq "${_expected}" ]]
}

@test "test_get_stack_trace" {
    run test
    _confirm_status
}

@test "test_base_path" {
    run test_base_path
    shell::confirm_success "${status}"
}

@test "test_base_name" {
    run test_base_name
    shell::confirm_success "${status}"
}

@test "test_offset_path" {
    run test_offset_path
    shell::confirm_success "${status}"
}
