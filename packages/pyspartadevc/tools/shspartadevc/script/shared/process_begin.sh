#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show_message.sh

initialize_text_file() (
    declare -r _header="$1"
    declare -r _shebang="#!/bin/bash"

    export_lines "${_shebang}" "${_header}"
)

_show_preprocess_log() (
    declare -r _group="$1"

    declare -r _path=$(shell::get_file_path)

    show_log "${_group}: ${_path}"
)

begin_text_file() (
    declare -r _group=$(constant::group_text_remove)

    _remove_preprocess_script() {
        declare -r path=$(shell::get_file_path)

        rm "${path}"
    }

    _execute_and_show() {
        _remove_preprocess_script
        _show_preprocess_log "${_group}"
    }

    _main() {
        declare -r path=$(shell::get_file_path)

        if [[ -e "${path}" ]]; then
            _execute_and_show
        fi
    }

    _main
)

end_text_file() (
    declare -r _group=$(constant::group_text_create)

    _add_executable_permission() {
        declare -r path=$(shell::get_file_path)

        chmod +x "${path}"
    }

    _execute_and_show() {
        _add_executable_permission
        _show_preprocess_log "${_group}"
    }

    _main() {
        declare -r path=$(shell::get_file_path)

        if [[ -e "${path}" ]]; then
            _execute_and_show
        fi
    }

    _main
)
