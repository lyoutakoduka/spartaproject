#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh

export_lines() (
    export_line() {
        declare -r _text="$1"

        declare -r path=$(shell::get_file_path)

        if [[ -n "${path}" ]]; then
            echo "${_text}" >>"${path}"
        fi
    }

    for text in "$@"; do
        export_line "${text}"
    done
)
