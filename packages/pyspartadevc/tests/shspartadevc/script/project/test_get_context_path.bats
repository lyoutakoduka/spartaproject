#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/project/test_get_context_path.sh
}

@test "test_base" {
    run test_base
    shell::confirm_success "${status}"
}

@test "test_forward" {
    run test_forward
    shell::confirm_success "${status}"
}
