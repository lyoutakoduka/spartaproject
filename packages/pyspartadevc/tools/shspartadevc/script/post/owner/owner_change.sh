#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_pair.sh

get_command_change() (
    declare -r _user_name="$1"
    declare -r _volume="$2"
    declare -r _change_main="sudo"
    declare -r _change_sub="chown"

    _get_change_pair() {
        declare -r text=$(create_pair "${_user_name}" "${_user_name}")
        echo "${text}"
    }

    _get_command_inside() {
        declare -r change_pair=$(_get_change_pair)
        echo "${change_pair} ${_volume}"
    }

    _get_command_change() {
        echo "${_change_main} ${_change_sub}"
    }

    _main() {
        declare -r command_change=$(_get_command_change)
        declare -r command_inside=$(_get_command_inside)

        echo "${command_change} ${command_inside}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
