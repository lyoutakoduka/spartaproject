#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_ready.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file_initialize.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_end.sh

_add_text_file_launch() (
    declare -r _expected="create"
    declare -r command_base="devcontainer up"
    declare -r _flag_exists="--remove-existing-container"
    declare -r _flag_config="--config"
    declare -r _flag_workspace="--workspace-folder"
    declare -r _group="$1"
    declare -r _message=$(constant::header_devcontainer)
    declare -r _enter=$(constant::enter)
    declare -r _indent=$(constant::indent)
    declare -r _config_path=$(constant::config)
    declare -r _current=$(constant::current)

    _add_command_head() {
        declare -r command="${command_base}${_enter}"
        export_lines "${command}"
    }

    _add_command_body() (
        declare -r command="${_indent}${_flag_exists}${_enter}"
        export_lines "${command}"
    )

    _get_command_config() (
        declare -r command="${_indent}${_flag_config} ${_config_path}"
        export_lines "${command}"
    )

    _get_command_workspace() (
        declare -r workspace="${_flag_workspace} ${_current}"
        declare -r command="${_indent}${workspace}${_enter}"
        export_lines "${command}"
    )

    _add_command_foot() {
        _get_command_workspace
        _get_command_config
    }

    _add_command_base() {
        _add_command_head

        if [[ "${_group}" = "${_expected}" ]]; then
            _add_command_body "${_group}"
        fi

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
