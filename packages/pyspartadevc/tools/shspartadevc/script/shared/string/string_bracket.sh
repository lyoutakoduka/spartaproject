#!/bin/bash

add_bracket() (
    declare -r _text="$1"

    _main() {
        echo "[${_text}]"
    }

    declare -r result=$(_main)
    echo "${result}"
)
