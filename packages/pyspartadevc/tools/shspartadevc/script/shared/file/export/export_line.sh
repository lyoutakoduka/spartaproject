#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh

export_line() (
    declare -r _text="$1"

    _add_text() {
        declare -r path=$(shell::get_file_path)
        echo "${_text}" >>"${path}"
    }

    _main() {
        declare -r path=$(shell::get_file_path)

        if [[ -n "${path}" ]]; then
            _add_text
        fi
    }

    _main
)
