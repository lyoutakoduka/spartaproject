#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/string/log_message.sh

test_fake() (
    declare -r _group="root"
    declare -r _group_sub="head"
    declare -r _message="fake"
    declare -r _time="1970-01-01T09:00:00Z"

    declare -r _result=$(get_message "${_group}" "${_group_sub}" "${_message}")
    declare -r _expected="${_time} [${_group}:${_group_sub}] ${_message}"

    shell::error_difference "${_result}" "${_expected}"
)

"$@"
