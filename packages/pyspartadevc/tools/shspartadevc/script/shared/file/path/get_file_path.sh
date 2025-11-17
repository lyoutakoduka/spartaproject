#!/bin/bash

#*  Return:
#*      (string): The file path placed on global scope.
#*
shell::get_file_path() {
    declare -g ADDED_FILE_PATH

    echo "${ADDED_FILE_PATH}"
}
