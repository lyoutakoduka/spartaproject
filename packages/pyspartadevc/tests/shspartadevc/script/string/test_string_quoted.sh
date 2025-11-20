#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh

_test_string_quoted() (
    declare -r _text="test"
    declare -r _quote="$1"

    declare -r _result=$(string_quoted "${_text}" "${_quote}")
    declare -r _expected="${_quote}${_text}${_quote}"

    shell::error_difference "${_result}" "${_expected}"
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
