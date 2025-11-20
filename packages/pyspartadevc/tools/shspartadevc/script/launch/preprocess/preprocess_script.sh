#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_ready.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file_initialize.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_end.sh

_add_text_file_launch() (
    declare -r _expected="create"
    declare -r _group="$1"
    declare -r _message=$(constant::header_devcontainer)

    _add_command_head() {
        declare -r command_devcontainer=$(get_command_devcontainer)
        export_lines "${command_devcontainer}"
    }

    _add_command_body() (
        if [[ "${_group}" = "${_expected}" ]]; then
            declare -r command_exists=$(get_command_exists)
            export_lines "${command_exists}"
        fi
    )

    _add_command_foot() {
        declare -r command_workspace=$(get_command_workspace)
        declare -r command_config=$(get_command_config)

        export_lines "${command_workspace}" "${command_config}"
    }

    _add_command_base() {
        _add_command_head
        _add_command_body "${_group}"
        _add_command_foot
    }

    _main() {
        ready_identifier
        export_lines "${_message}"
        _add_command_base
    }

    _main
)

create_preprocess_script() (
    declare -r _expected="create"
    declare -r _group="$1"
    declare -r _script_create=$(constant::temporary_create)
    declare -r _script_attach=$(constant::temporary_attach)
    declare -r _header_create=$(constant::header_create)
    declare -r _header_attach=$(constant::header_attach)

    _get_preprocess() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_script_create}"
        else
            echo "${_script_attach}"
        fi
    }

    _get_header() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_header_create}"
        else
            echo "${_header_attach}"
        fi
    }

    _whole_text_file() {
        begin_text_file

        declare -r header=$(_get_header)
        initialize_text_file "${header}"
        _add_text_file_launch "${_group}"

        end_text_file
    }

    _main() {
        declare -r path=$(_get_preprocess)
        shell::set_file_path "${path}"

        _whole_text_file
    }

    _main
)
