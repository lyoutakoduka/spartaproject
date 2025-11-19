#!/bin/bash

create_pair_comment() (
    declare -r _key="$1"
    declare -r _value="$2"

    echo "${_key}: ${_value}"
)
