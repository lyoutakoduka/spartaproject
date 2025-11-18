#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/constant/test_constant_filter.sh
}

@test "test_filter" {
    run test_filter
    shell::confirm_success "${status}"
}
