#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

command_change_owner() (
    declare -r _command_change="sudo chown"
    declare -r _cache=$(constant::volume_cache)
    declare -r _python=$(constant::volume_python)
    declare -r _javascript=$(constant::volume_javascript)
    declare -r _comment=$(constant::comment_owner)

    _change_owner() {
        declare -r volume="$1"

        declare -r user_name=$(whoami)
        declare -r _change_pair="${user_name}:${user_name}"
        declare -r command="${_command_change} ${_change_pair} ${volume}"

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
