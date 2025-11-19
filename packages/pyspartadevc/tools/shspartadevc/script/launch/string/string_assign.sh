#!/bin/bash

create_assign() (
    declare -r _key="$1"
    declare -r _value="$2"

    echo "${_key}=${_value}"
)
