#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_exists.sh
. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh

test_root() (
    declare -r _group_root="test_handle/root"

    _main() {
        declare -r temporary=$(begin_temporary_root "${_group_root}")
        shell::error_no_exists "${temporary}"

        end_temporary_root "${temporary}"
        shell::error_exists "${temporary}"
    }

    _main
)

"$@"
