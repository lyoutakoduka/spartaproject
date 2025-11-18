#!/bin/bash

#*  Args:
#*      $1 (string): The value of test result.
#*
#*      $2 (string): Expected value for test.
#*
#*  Error:
#*      exit 1, if two values are different.
#*
shell::error_difference() {
    declare -r _result="$1"
    declare -r _expected="$2"

    if [[ "${_result}" != "${_expected}" ]]; then
        exit 1
    fi
}

#*  Args:
#*      $1 (string): The value of test result.
#*
#*      $2 (string): Expected value for test.
#*
#*  Error:
#*      exit 1, if two values are different.
#*
shell::error_same() {
    declare -r _result="$1"
    declare -r _expected="$2"

    if [[ "${_result}" == "${_expected}" ]]; then
        exit 1
    fi
}
