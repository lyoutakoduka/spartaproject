#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh

export_lines() (
    declare -r _arguments=("$@")

    declare -r path=$(shell::get_file_path)

    if [[ -n "${path}" ]]; then
        for text in "${_arguments[@]}"; do
            echo "${text}" >>"${path}"
        done
    fi
)

shell::get_file_path() {
    declare -g ADDED_FILE_PATH

    echo "${ADDED_FILE_PATH}"
}

shell::set_file_path() {
    declare -r path="$1"

    declare -g ADDED_FILE_PATH="${path}"
}

_show_message() (
    declare -r _group="$1"
    declare -r _message="$2"
    declare -r _package=$(constant::package_main)

    echo "[${_package}:${_group}] ${_message}"
)

shell::show_warning() {
    declare -r _message="$1"
    declare -r _group="error"

    _show_message "${_group}" "${_message}"

    exit 1
}

show_log() (
    declare -r _message="$1"
    declare -r _group="log"

    _show_message "${_group}" "${_message}"
)
