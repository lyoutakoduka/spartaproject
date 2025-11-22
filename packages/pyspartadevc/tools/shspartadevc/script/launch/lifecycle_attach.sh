#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/string/log_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/shared_launch.sh

declare -g FFB275A

lifecycle_attach() (
    declare -r _message=$(constant::help_attach)

    if [[ "${FFB275A}" == "true" ]]; then
        show_log "${_message}"
    else
        show_log "${_message}"
    fi

    zsh
)
