#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/bats/test_confirm_status.sh
}

@test "test_success" {
    run test_success
    shell::confirm_success "${status}"
}

@test "test_error" {
    run test_error
    shell::confirm_error "${status}"
}
