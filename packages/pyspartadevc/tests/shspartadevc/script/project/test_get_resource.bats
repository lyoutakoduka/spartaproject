#!/usr/bin/env bats

. packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
. packages/pyspartadevc/tests/shspartadevc/script/project/test_get_resource.sh

@test "test_base" {
    run test_base
    shell::confirm_success "${status}"
}

@test "test_local" {
    run test_local
    shell::confirm_success "${status}"
}
