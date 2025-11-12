#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

get_command_exists() (
    declare -r _flag_exists=$(constant::flag_exists)
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    _main() {
        echo "${_indent}${_flag_exists}${_enter}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
