#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/path/test_path_temporary.sh
}

@test "test_file" {
    run test_file
    shell::confirm_success "${status}"
}

@test "test_directory" {
    run test_directory
    shell::confirm_success "${status}"
}
