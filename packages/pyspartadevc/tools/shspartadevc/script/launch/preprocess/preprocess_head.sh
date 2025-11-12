#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/file_initialize.sh

head_text_file() (
    declare -r _group="$1"
    declare -r _expected=$(constant::group_create)
    declare -r _header_create=$(constant::header_create)
    declare -r _header_attach=$(constant::header_attach)

    _get_header() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_header_create}"
        else
            echo "${_header_attach}"
        fi
    }

    _main() {
        declare -r header=$(_get_header)
        initialize_text_file "${header}"
    }

    _main
)
