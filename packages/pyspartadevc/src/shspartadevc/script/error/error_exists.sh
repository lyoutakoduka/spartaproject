#!/bin/bash

shell::error_no_exists() {
    declare -r _path="$1"

    if [[ ! -e "${_path}" ]]; then
        exit 1
    fi
}

shell::error_exists() {
    declare -r _path="$1"

    if [[ -e "${_path}" ]]; then
        exit 1
    fi
}
