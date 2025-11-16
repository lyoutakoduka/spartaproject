#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh

_test_string_quoted() (
    declare -r _text="test"
    declare -r _quote="$1"

    _get_result() {
        declare -r result=$(string_quoted "${_text}" "${_quote}")
        echo "${result}"
    }

    _get_expected() {
        echo "${_quote}${_text}${_quote}"
    }

    _main() {
        declare -r result=$(_get_result)
        declare -r expected=$(_get_expected)

        shell::error_difference "${result}" "${expected}"
    }

    _main
)

test_single() (
    declare -r _quote="'"

    _test_string_quoted "${_quote}" || exit 1
)

test_double() (
    declare -r _quote="\""

    _test_string_quoted "${_quote}" || exit 1
)

"$@"
