#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/owner/owner_change.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/owner/owner_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

create_command_owner() (
    declare -r _cache=$(constant::volume_cache)
    declare -r _python=$(constant::volume_python)
    declare -r _javascript=$(constant::volume_javascript)

    _change_owner() {
        declare -r volume="$1"

        declare -r user_name=$(whoami)
        declare -r command=$(get_command_change "${user_name}" "${volume}")

        export_line "${command}"
    }

    _main() {
        add_owner_comment

        _change_owner "${_cache}"
        _change_owner "${_python}"
        _change_owner "${_javascript}"
    }

    _main
)
