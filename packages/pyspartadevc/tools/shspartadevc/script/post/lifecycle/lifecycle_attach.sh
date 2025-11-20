#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show_message.sh

lifecycle_attach() (
    declare -r _message=$(constant::help_attach)

    show_log "${_message}"

    zsh
)
