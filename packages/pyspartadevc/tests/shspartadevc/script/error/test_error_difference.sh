#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

test_difference() (
    declare -r _expected="test"
    shell::error_difference "${_expected}" "${_expected}"
)

test_same() (
    declare -r _expected="test"
    declare -r _result="error"

    shell::error_same "${_result}" "${_expected}"
)

"$@"
