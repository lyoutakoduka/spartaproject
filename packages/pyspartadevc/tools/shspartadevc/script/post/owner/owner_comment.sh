#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

add_owner_comment() (
    declare -r _comment=$(constant::comment_owner)

    export_line "${_comment}"
)
