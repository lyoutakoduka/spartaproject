#!/bin/bash

create_assign() (
    declare -r _key="$1"
    declare -r _value="$2"

    _main() {
        echo "${_key}=${_value}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
