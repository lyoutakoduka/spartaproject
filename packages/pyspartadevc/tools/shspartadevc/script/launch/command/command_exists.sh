#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_command_exists() (
    declare -r _flag_exists="--remove-existing-container"
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    echo "${_indent}${_flag_exists}${_enter}"
)
