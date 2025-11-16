#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh

_lifecycle() (
    declare -r _message=$(constant::help_attach)

    show_log "${_message}"
    zsh
)

_lifecycle
