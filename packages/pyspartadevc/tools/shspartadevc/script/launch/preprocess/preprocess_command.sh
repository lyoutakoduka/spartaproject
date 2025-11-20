#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_command_exists() (
    declare -r _flag_exists="--remove-existing-container"
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    echo "${_indent}${_flag_exists}${_enter}"
)

get_command_devcontainer() (
    declare -r command_base="devcontainer up"
    declare -r _enter=$(constant::enter)

    echo "${command_base}${_enter}"
)
