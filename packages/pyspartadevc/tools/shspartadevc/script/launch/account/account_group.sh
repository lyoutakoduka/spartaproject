#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh

get_group_identifier() (
    declare -r _option=$(constant::identifier_group)

    declare -r -i identifier=$(id "${_option}")
    echo "${identifier}"
)
