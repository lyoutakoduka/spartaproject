#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_log.sh

end_text_file() (
    declare -r _group=$(constant::group_text_create)

    _add_executable_permission() {
        declare -r path=$(shell::get_file_path)

        chmod +x "${path}"
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
