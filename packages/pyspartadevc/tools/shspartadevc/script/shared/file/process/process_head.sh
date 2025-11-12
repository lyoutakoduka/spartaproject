#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_comment.sh

show_preprocess_log() (
    declare -r _group="$1"

    _get_pair_log() {
        declare -r path=$(get_file_path)
        declare -r text=$(create_pair_comment "${_group}" "${path}")

        echo "${text}"
    }

    _main() {
        declare -r pair_log=$(_get_pair_log)
        show_log "${pair_log}"
    }

    _main
)
