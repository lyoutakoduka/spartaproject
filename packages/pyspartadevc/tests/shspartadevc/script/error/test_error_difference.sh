#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

test_difference() (
    declare -r _expected="test"

    shell::error_difference "${_expected}" "${_expected}"
)

"$@"
