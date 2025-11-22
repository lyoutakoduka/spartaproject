#!/usr/bin/env bats

setup() {
    . packages/pyspartadevc/src/shspartadevc/script/bats/confirm_status.sh
    . packages/pyspartadevc/tests/shspartadevc/script/string/test_log_message.sh
}

@test "test_fake" {
    run test_fake
    shell::confirm_success "${status}"
}
