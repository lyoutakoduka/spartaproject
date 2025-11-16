#!/usr/bin/env bats

test_success() (
    exit 0
)

test_error() (
    exit 1
)

"$@"
