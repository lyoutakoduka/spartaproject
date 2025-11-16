#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_same.sh

test() (
    declare -r _expected="test"
    declare -r _result="error"

    shell::error_same "${_result}" "${_expected}"
)

"$@"
