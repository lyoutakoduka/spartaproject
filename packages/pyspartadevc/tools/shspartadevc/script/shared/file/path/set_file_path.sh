#!/bin/bash

#*  Args:
#*      _path (string): Set the file path placed on global scope.
#*
shell::set_file_path() {
    declare -r path="$1"

    # shellcheck disable=SC2034
    declare -g ADDED_FILE_PATH="${path}"
}
