#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

test() (
    declare -r _expected="test"

    shell::error_difference "${_expected}" "${_expected}"
)

"$@"
