#!/bin/bash

error_difference() {
    declare -r _status=1
    declare -r _result="$1"
    declare -r _expected="$2"

    _main() {
        if [[ "${_result}" != "${_expected}" ]]; then
            exit "${_status}"
        fi
    }

    _main
}
