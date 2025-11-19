#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_command_devcontainer() (
    declare -r _command_main="devcontainer"
    declare -r _command_sub="up"
    declare -r _enter=$(constant::enter)

    _get_command_base() {
        echo "${_command_main} ${_command_sub}"
    }

    _main() {
        declare -r command_base=$(_get_command_base)
        echo "${command_base}${_enter}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
