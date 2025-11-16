#!/bin/bash

string_quoted() (
    declare -r _text="$1"
    declare -r _quote="$2"

    echo "${_quote}${_text}${_quote}"
)
