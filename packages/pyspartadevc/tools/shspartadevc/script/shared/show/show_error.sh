#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_message.sh

show_error() (
    declare -r _message="$1"
    declare -r _group=$(constant::group_error)

    _main() {
        show_message "${_group}" "${_message}"
    }

    _main
)
