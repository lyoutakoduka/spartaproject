#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_comment.sh

command_package_manager() (
    declare -r _sync_python="uv sync"
    declare -r _sync_javascript="yarn"
    declare -r _comment=$(constant::comment_sync)

    export_lines "${_comment}" "${_sync_python}" "${_sync_javascript}"
)
