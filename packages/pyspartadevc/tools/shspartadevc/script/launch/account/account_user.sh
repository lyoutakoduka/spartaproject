#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh

get_user_identifier() (
    declare -r _option=$(constant::identifier_user)

    id "${_option}"
)
