#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_ready.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/command/command_config.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/command/command_devcontainer.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/command/command_exists.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/command/command_workspace.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_lines.sh

_filter_exists_command() (
    declare -r _expected="create"
    declare -r _group="$1"

    _add_section_exists() {
        declare -r command_exists=$(get_command_exists)
        export_line "${command_exists}"
    }

    _main() {
        if [[ "${_group}" = "${_expected}" ]]; then
            _add_section_exists
        fi
    }

    _main
)

body_text_file() (
    declare -r _group="$1"
    declare -r _message=$(constant::header_devcontainer)

    _add_shared_head() {
        declare -r command_devcontainer=$(get_command_devcontainer)
        export_line "${command_devcontainer}"
    }

    _add_shared_foot() {
        declare -r command_workspace=$(get_command_workspace)
        declare -r command_config=$(get_command_config)

        export_lines "${command_workspace}" "${command_config}"
    }

    _add_command_base() {
        _add_shared_head
        _filter_exists_command "${_group}"
        _add_shared_foot
    }

    _main() {
        ready_identifier
        export_line "${_message}"
        _add_command_base
    }

    _main
)
