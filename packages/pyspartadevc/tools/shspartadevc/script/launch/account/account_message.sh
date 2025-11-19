#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh

show_identifier() (
    declare -r _status="$1"
    declare -r _success="true"
    declare -r _identifier=$(constant::message_identifier)

    _show_message_identifier() {
        show_log "${_identifier}"
    }

    _main() {
        if [[ "${_status}" = "${_success}" ]]; then
            _show_message_identifier
        fi
    }

    _main
)
