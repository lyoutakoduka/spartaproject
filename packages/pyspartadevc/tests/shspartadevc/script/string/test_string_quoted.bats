#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/string/test_string_quoted.sh
}

@test "test_single" {
    run test_single
    shell::confirm_success "${status}"
}

@test "test_double" {
    run test_double
    shell::confirm_success "${status}"
}
