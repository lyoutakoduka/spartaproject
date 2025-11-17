#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh

#*  Return:
#*      (string): Group Identifier (GID).
#*
get_group_identifier() (
    declare -r _option=$(constant::identifier_group)

    id "${_option}"
)
