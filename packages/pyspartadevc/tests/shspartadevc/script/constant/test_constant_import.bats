#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/constant/test_constant_import.sh
}

@test "test_import" {
    run test_import
    shell::confirm_success "${status}"
}
