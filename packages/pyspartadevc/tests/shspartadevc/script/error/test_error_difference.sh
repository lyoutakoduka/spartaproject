#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh

test() (
    declare -r _expected="test"

    error_difference "${_expected}" "${_expected}"
)

"$@"
