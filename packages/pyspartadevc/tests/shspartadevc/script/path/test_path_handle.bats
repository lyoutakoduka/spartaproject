#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/path/test_path_handle.sh
}

@test "test_root" {
    run test_root
    shell::confirm_success "${status}"
}
