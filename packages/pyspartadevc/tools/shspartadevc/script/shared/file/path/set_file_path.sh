#!/bin/bash

set_file_path() {
    declare -r path="$1"

    declare -g ADDED_FILE_PATH="${path}"
}
