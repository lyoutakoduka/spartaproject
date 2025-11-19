#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_pair.sh

show_message() (
    declare -r _group="$1"
    declare -r _message="$2"
    declare -r _package=$(constant::package_main)

    declare -r _message_inside=$(create_pair "${_package}" "${_group}")
    echo "[${_message_inside}] ${_message}"
)
