#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_pair.sh

get_command_change() (
    declare -r _command_change="sudo chown"
    declare -r _user_name="$1"
    declare -r _volume="$2"

    declare -r _change_pair=$(create_pair "${_user_name}" "${_user_name}")
    echo "${_command_change} ${_change_pair} ${_volume}"
)
