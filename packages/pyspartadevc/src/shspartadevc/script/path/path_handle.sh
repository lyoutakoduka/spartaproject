#!/bin/bash

begin_temporary_root() {
    declare -r _package="/tmp/pyspartadevc"
    declare -r _group_root="$1"

    declare -r temporary="${_package}/${_group_root}"
    mkdir --parents "${temporary}"

    echo "${temporary}"
}
