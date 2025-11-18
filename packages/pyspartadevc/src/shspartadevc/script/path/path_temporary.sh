#!/bin/bash

_add_path_identifier() (
    declare -r _identifier="XXXXXXXX"
    declare -r _path_head="$1"

    echo "${_path_head}#${_identifier}"
)
