#!/usr/bin/env bats

. packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
. packages/pyspartadevc/tests/shspartadevc/script/project/test_get_stack_trace.sh

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

@test "test_offset_name" {
    run test_offset_name
    shell::confirm_success "${status}"
}
