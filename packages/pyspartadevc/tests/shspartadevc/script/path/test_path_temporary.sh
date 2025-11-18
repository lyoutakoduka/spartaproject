#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh

_cleanup_temporary_root() (
    declare -r _temporary="$1"

    declare -r parent=$(dirname "${_temporary}")
    end_temporary_root "${parent}"
)
