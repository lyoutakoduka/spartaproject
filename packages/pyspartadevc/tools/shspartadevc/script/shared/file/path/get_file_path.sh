#!/bin/bash

shell::get_file_path() {
    declare -g ADDED_FILE_PATH

    echo "${ADDED_FILE_PATH}"
}

shell::set_file_path() {
    declare -r path="$1"

    # shellcheck disable=SC2034
    declare -g ADDED_FILE_PATH="${path}"
}
