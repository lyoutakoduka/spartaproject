#!/bin/bash

filter_constant() (
    declare -r _text_json="$1"
    declare -r _filter="$2"

    declare -r result=$(echo "${_text_json}" | jq -r ".${_filter}")

    echo "${result}"
)
