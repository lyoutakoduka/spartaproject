#!/usr/bin/env bats

. packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
. packages/pyspartadevc/tests/shspartadevc/script/project/test_get_context_path.sh

_confirm_status() {
    declare -r _expected=0
    [[ "${status}" -eq "${_expected}" ]]
}

@test "test_get_context_path" {
    run test
    _confirm_status
}

@test "test_base" {
    run test_base
    shell::confirm_success "${status}"
}
