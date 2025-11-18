#!/bin/bash

#*  Args:
#*      $1 (string): Json formatted text.
#*
#*      $2 (string): Group key used to filter the text.
#*
#*  Return:
#*      (string) Json formatted text filtered by group key.
#*
filter_constant() (
    declare -r _text_json="$1"
    declare -r _filter="$2"

    declare -r result=$(echo "${_text_json}" | jq -r ".${_filter}")

    echo "${result}"
)
