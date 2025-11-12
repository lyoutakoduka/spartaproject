#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/sync/sync_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

create_command_sync() (
    declare -r _python_main=$(constant::sync_python_main)
    declare -r _python_sub=$(constant::sync_python_sub)
    declare -r _javascript=$(constant::sync_javascript)

    _get_sync_python() {
        echo "${_python_main} ${_python_sub}"
    }

    _add_package_managers() {
        for command in "$@"; do
            export_line "${command}"
        done
    }

    _get_package_managers() {
        declare -r sync_python=$(_get_sync_python)
        _add_package_managers "${_javascript}" "${sync_python}"
    }

    _main() {
        add_comment_sync
        _get_package_managers
    }

    _main
)
