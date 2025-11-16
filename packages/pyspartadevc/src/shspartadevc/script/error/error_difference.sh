#!/bin/bash

shell::error_difference() {
    declare -r _result="$1"
    declare -r _expected="$2"

    if [[ "${_result}" != "${_expected}" ]]; then
        exit 1
    fi
}
