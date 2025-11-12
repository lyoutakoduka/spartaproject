#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh

get_command_devcontainer() (
    declare -r _command_main=$(constant::devcontainer_main)
    declare -r _command_sub=$(constant::devcontainer_sub)
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
