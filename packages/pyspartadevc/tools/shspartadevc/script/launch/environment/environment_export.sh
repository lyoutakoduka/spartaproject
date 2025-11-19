#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

export_environment() (
    declare -r _command="export"
    declare -r _key="$1"
    declare -r _value="$2"

    export_lines "${_command} ${_key}=${_value}"
)
