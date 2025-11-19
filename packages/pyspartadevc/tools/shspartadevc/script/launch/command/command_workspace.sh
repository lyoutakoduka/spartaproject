#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

get_command_workspace() (
    declare -r _flag_workspace="--workspace-folder"
    declare -r _current="."
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    _get_workspace_section() {
        echo "${_flag_workspace} ${_current}"
    }

    _main() {
        declare -r workspace=$(_get_workspace_section)
        echo "${_indent}${workspace}${_enter}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
