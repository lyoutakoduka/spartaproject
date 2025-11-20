#!/bin/bash

if [[ "${FF_0000_TOP}" = "true" ]]; then
    . packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh
    . packages/pyspartadevc/src/shspartadevc/script/path/path_temporary.sh
    . packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
fi

export_lines() (
    declare -r _arguments=("$@")

    declare -r path=$(shell::get_file_path)

    if [[ -n "${path}" ]]; then
        for text in "${_arguments[@]}"; do
            echo "${text}" >>"${path}"
        done
    fi
)

shell::get_file_path() {
    declare -g ADDED_FILE_PATH

    echo "${ADDED_FILE_PATH}"
}

shell::set_file_path() {
    declare -r path="$1"

    declare -g ADDED_FILE_PATH="${path}"
}

_show_message() (
    declare -r _group="$1"
    declare -r _message="$2"
    declare -r _package=$(constant::package_main)

    echo "[${_package}:${_group}] ${_message}"
)

shell::show_warning() {
    declare -r _message="$1"
    declare -r _group="error"

    _show_message "${_group}" "${_message}"

    exit 1
}

show_log() (
    declare -r _message="$1"
    declare -r _group="log"

    _show_message "${_group}" "${_message}"
)

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
