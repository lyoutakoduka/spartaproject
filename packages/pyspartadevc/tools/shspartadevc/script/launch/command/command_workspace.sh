#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

get_command_workspace() (
    declare -r _flag_workspace="--workspace-folder"
    declare -r _current=$(constant::current)
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    declare -r workspace="${_flag_workspace} ${_current}"
    echo "${_indent}${workspace}${_enter}"
)
