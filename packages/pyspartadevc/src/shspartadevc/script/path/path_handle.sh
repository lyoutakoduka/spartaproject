#!/bin/bash

#*  Args:
#*      $1 (string): The relative path inside of package directory.
#*
#*  Return:
#*      (string): The path to the created package directory.
#*
begin_temporary_root() {
    declare -r _package="/tmp/pyspartadevc"
    declare -r _group_root="$1"

    declare -r temporary="${_package}/${_group_root}"
    mkdir --parents "${temporary}"

    echo "${temporary}"
}

#*  Args:
#*      $1 (string): The path you want to clean up.
#*
end_temporary_root() {
    declare -r _temporary="$1"

    rm --recursive --force "${_temporary}"
}
