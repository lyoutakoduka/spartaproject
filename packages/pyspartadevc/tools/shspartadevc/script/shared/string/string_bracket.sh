#!/bin/bash

add_bracket() (
    declare -r _text="$1"

    echo "[${_text}]"
)
