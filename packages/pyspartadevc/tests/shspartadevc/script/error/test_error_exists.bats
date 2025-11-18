#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/error/test_error_exists.sh
}

@test "test_no_exists" {
    run test_no_exists
    shell::confirm_success "${status}"
}

@test "test_exists" {
    run test_exists
    shell::confirm_success "${status}"
}
