#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/error/test_error_same.sh
}

@test "test_error_same" {
    run test_same
    shell::confirm_success "${status}"
}
