#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/sync/sync_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

create_command_sync() (
    declare -r _sync_python="uv sync"
    declare -r _sync_javascript="yarn"

    add_comment_sync

    export_line "${_sync_python}"
    export_line "${_sync_javascript}"
)
