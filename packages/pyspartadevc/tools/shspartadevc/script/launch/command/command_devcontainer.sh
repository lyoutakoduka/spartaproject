#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

get_command_devcontainer() (
    declare -r command_base="devcontainer up"
    declare -r _enter=$(constant::enter)

    echo "${command_base}${_enter}"
)
