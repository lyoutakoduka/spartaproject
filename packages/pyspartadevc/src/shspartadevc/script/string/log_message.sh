#!/bin/bash

#*  Args:
#*      $1 (string): Main group name used for log message.
#*
#*      $2 (string): Sub group name used for log message.
#*
#*      $3 (string): Text used for log message.
#*
#*  Return:
#*      (string): Log message string with timestamp and group information.
#*
get_message() (
    declare -r _format="seconds"
    declare -r _zone="Asia/Tokyo"
    declare -r _format="%Y-%m-%dT%H:%M:%SZ"
    declare -r _group_main="$1"
    declare -r _group_sub="$2"
    declare -r _message="$3"

    _get_time() {
        if [[ "${_message}" == "fake" ]]; then
            date +"${_format}" --date @0
        else
            date +"${_format}"
        fi
    }

    _main() {
        TZ="${_zone}"
        declare -r time=$(_get_time)

        echo "${time} [${_group_main}:${_group_sub}] ${_message}"
    }

    _main
)
