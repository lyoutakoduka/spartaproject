#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_comment.sh

#*  Args:
#*      _group (string): Set the file path placed on global scope.
#*
show_preprocess_log() (
    declare -r _group="$1"

    declare -r _path=$(shell::get_file_path)

    show_log "${_group}: ${_path}"
)
