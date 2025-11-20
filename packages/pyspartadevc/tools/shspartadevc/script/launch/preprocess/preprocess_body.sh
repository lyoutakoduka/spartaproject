#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_ready.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

body_text_file() (
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
