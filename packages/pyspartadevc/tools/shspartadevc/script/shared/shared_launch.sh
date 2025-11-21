#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh
. packages/pyspartadevc/src/shspartadevc/script/path/path_temporary.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh

export_lines() (
    declare -r _arguments=("$@")
    declare -g ADDED_FILE_PATH

    if [[ -n "${ADDED_FILE_PATH}" ]]; then
        for text in "${_arguments[@]}"; do
            echo "${text}" >>"${ADDED_FILE_PATH}"
        done
    fi
)

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

shell::begin_text_file() {
    declare -r _group="preprocess"
    declare -r _head="devcontainer"
    declare -r _suffix="sh"

    declare -r _temporary=$(
        get_temporary_file "${_group}" "${_head}" "${_suffix}"
    )
    declare -g ADDED_FILE_PATH="${_temporary}"
}

end_text_file() {
    declare -g ADDED_FILE_PATH
    declare -r _script_path="$1"
    declare -r _group=$(constant::group_text_create)

    _main() {
        mv --force "${ADDED_FILE_PATH}" "${_script_path}"
        chmod +x "${_script_path}"
        show_log "${_group}: ${_script_path}"
    }

    _main
}
