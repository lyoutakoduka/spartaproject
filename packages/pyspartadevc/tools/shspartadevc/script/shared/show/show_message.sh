#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

show_message() (
    declare -r _group="$1"
    declare -r _message="$2"
    declare -r _package=$(constant::package_main)

    echo "[${_package}:${_group}] ${_message}"
)

shell::show_warning() {
    declare -r _message="$1"
    declare -r _group="error"

    show_message "${_group}" "${_message}"

    exit 1
}

show_log() (
    declare -r _message="$1"
    declare -r _group="log"

    show_message "${_group}" "${_message}"
)
