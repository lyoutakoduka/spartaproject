#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh

add_double_quote() (
    declare -r _text="$1"
    declare -r _quote=$(constant::quote)

    _main() {
        echo "${_quote}${_text}${_quote}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
