#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_log.sh

#*  Set executable permission to the script for dev-container, and log it.
#*
end_text_file() (
    declare -r _group=$(constant::group_text_create)
    declare -r _executable_sub=$(constant::executable_sub)

    _add_executable_permission() {
        declare -r path=$(shell::get_file_path)
        declare -r _command="${_executable_sub}"

        chmod "${_command}" "${path}"
    }

    _execute_and_show() {
        _add_executable_permission
        show_preprocess_log "${_group}"
    }

    _main() {
        declare -r path=$(shell::get_file_path)

        if [[ -e "${path}" ]]; then
            _execute_and_show
        fi
    }

    _main
)
