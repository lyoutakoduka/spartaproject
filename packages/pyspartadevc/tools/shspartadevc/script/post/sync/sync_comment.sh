#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

add_comment_sync() (
    declare -r _comment=$(constant::comment_sync)

    _main() {
        export_line "${_comment}"
    }

    _main
)
