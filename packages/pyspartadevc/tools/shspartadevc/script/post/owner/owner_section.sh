#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/owner/owner_change.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/owner/owner_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

create_command_owner() (
    declare -r _cache="cache"
    declare -r _temporary=".temp"
    declare -r _python=".venv"
    declare -r _javascript="node_modules"

    _change_owner() {
        declare -r user_name="$1"
        declare -r volume="$2"

        declare -r command=$(get_command_change "${user_name}" "${volume}")

        export_line "${command}"
    }

    _change_owners() {
        declare -r user_name=$(whoami)

        for volume in "$@"; do
            _change_owner "${user_name}" "${volume}"
        done
    }

    _get_volume_cache() {
        echo "${_temporary}/${_cache}"
    }

    _add_owner_change() {
        declare -r cache=$(_get_volume_cache)
        _change_owners "${cache}" "${_python}" "${_javascript}"
    }

    _main() {
        add_owner_comment
        _add_owner_change
    }

    _main
)
