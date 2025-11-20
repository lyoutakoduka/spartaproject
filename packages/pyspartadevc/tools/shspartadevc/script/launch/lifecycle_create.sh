#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/shared_launch.sh

_command_change_owner() (
    declare -r _command_change="sudo chown"
    declare -r _cache=$(constant::volume_cache)
    declare -r _python=$(constant::volume_python)
    declare -r _javascript=$(constant::volume_javascript)
    declare -r _comment=$(constant::comment_owner)

    _change_owner() {
        declare -r volume="$1"

        declare -r user_name=$(whoami)
        declare -r change_pair="${user_name}:${user_name}"
        declare -r command="${_command_change} ${change_pair} ${volume}"

        export_lines "${command}"
    }

    _main() {
        export_lines "${_comment}"

        _change_owner "${_cache}"
        _change_owner "${_python}"
        _change_owner "${_javascript}"
    }

    _main
)

_command_package_manager() (
    declare -r _sync_python="uv sync"
    declare -r _sync_javascript="yarn"
    declare -r _comment=$(constant::comment_sync)

    export_lines "${_comment}" "${_sync_python}" "${_sync_javascript}"
)

lifecycle_create() (
    declare -r _header=$(constant::header_post)
    declare -r _script_post=$(constant::temporary_post)

    _add_text_file_post() {
        _command_change_owner
        _command_package_manager
    }

    _whole_text_file() {
        begin_text_file

        initialize_text_file "${_header}"
        _add_text_file_post

        end_text_file
    }

    _main() {
        shell::set_file_path "${_script_post}"
        _whole_text_file
    }

    _main
)
