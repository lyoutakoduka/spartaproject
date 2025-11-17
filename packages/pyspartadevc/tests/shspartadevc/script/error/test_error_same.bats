#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/tests/shspartadevc/script/error/test_error_same.sh
}

_confirm_status() {
    declare -r _expected=0
    [[ "${status}" -eq "${_expected}" ]]
}

@test "test_error_same" {
    run test
    _confirm_status
}
