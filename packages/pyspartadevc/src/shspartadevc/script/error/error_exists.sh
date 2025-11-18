#!/bin/bash

#*  Args:
#*      $1 (string): The path you want to confirm existing.
#*
#*  Error:
#*      exit 1, if the path does not exists.
#*
shell::error_no_exists() {
    declare -r _path="$1"

    if [[ ! -e "${_path}" ]]; then
        exit 1
    fi
}

#*  Args:
#*      $1 (string): The path you want to confirm existing.
#*
#*  Error:
#*      exit 1, if the path is exists.
#*
shell::error_exists() {
    declare -r _path="$1"

    if [[ -e "${_path}" ]]; then
        exit 1
    fi
}
