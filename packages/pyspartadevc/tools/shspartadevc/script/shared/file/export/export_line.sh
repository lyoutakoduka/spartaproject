#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh

export_lines() (
    declare -r _arguments=("$@")

    declare -r path=$(shell::get_file_path)

    if [[ -n "${path}" ]]; then
        for text in "${_arguments[@]}"; do
            echo "${text}" >>"${path}"
        done
    fi
)
