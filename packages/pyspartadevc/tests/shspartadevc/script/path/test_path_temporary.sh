#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_exists.sh
. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh
. packages/pyspartadevc/src/shspartadevc/script/path/path_temporary.sh

_cleanup_temporary_root() (
    declare -r _temporary="$1"

    declare -r parent=$(dirname "${_temporary}")
    end_temporary_root "${parent}"
)

test_file() (
    declare -r _group_root="test_temporary/file"
    declare -r _path_head="path_test"
    declare -r _suffix="txt"

    _main() {
        declare -r temporary=$(
            get_temporary_file "${_group_root}" "${_path_head}" "${_suffix}"
        )

        shell::error_no_exists "${temporary}"
        _cleanup_temporary_root "${temporary}"
    }

    _main
)

"$@"
