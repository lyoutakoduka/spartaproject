#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_exists.sh

test_no_exists() (
    declare -r _path="packages/pyspartadevc"

    shell::error_no_exists "${_path}"
)

"$@"
