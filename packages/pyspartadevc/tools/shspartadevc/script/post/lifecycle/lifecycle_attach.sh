#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_log.sh

_lifecycle() (
    declare -r _terminal=$(constant::terminal)
    declare -r _message=$(constant::help_attach)

    _launch_terminal() {
        eval "${_terminal}"
    }

    _main() {
        show_log "${_message}"
        _launch_terminal
    }

    _main
)

_lifecycle
