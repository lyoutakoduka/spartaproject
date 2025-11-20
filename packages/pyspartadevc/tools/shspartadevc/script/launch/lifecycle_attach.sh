#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/shared_launch.sh

lifecycle_attach() (
    declare -r _message=$(constant::help_attach)

    show_log "${_message}"

    zsh
)
