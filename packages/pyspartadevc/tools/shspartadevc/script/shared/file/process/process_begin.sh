#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_log.sh

#*  Remove the script for dev-container, and log it.
#*
begin_text_file() (
    declare -r _group=$(constant::group_text_remove)

    _remove_preprocess_script() {
        declare -r path=$(get_file_path)

        rm "${path}"
    }

    _execute_and_show() {
        _remove_preprocess_script
        show_preprocess_log "${_group}"
    }

    _main() {
        declare -r path=$(get_file_path)

        if [[ -e "${path}" ]]; then
            _execute_and_show
        fi
    }

    _main
)
