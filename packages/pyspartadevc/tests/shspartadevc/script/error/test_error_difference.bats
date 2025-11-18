#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/error/test_error_difference.sh
}

@test "test_difference" {
    run test_difference
    shell::confirm_success "${status}"
}

@test "test_same" {
    run test_same
    shell::confirm_success "${status}"
}
