#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_bracket.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/string/string_pair.sh

show_message() (
    declare -r _group="$1"
    declare -r _message="$2"
    declare -r _package="pyspartadevc"

    _get_message_inside() {
        declare -r text=$(create_pair "${_package}" "${_group}")

        echo "${text}"
    }

    _get_message_pair() {
        declare -r message_inside=$(_get_message_inside)
        declare -r text=$(add_bracket "${message_inside}")

        echo "${text}"
    }

    _main() {
        declare -r message_pair=$(_get_message_pair)
        echo "${message_pair} ${_message}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
