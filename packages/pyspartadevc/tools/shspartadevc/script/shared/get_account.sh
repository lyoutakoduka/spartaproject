#!/bin/bash

get_user_name() (
    declare -r _user_name=$(whoami)

    _main() {
        echo "${_user_name}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
