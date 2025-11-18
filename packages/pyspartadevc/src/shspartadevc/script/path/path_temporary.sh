#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh

_add_path_identifier() (
    declare -r _identifier="XXXXXXXX"
    declare -r _path_head="$1"

    echo "${_path_head}#${_identifier}"
)

get_temporary_file() (
    declare -r _group_root="$1"
    declare -r _path_head="$2"
    declare -r _suffix="$3"

    _make_temporary() {
        declare -r temporary="$1"

        declare -r name=$(_add_path_identifier "${_path_head}")
        mktemp --tmpdir="${temporary}" --suffix=".${_suffix}" "${name}"
    }

    _main() {
        declare -r temporary=$(begin_temporary_root "${_group_root}")
        _make_temporary "${temporary}"
    }

    _main
)
