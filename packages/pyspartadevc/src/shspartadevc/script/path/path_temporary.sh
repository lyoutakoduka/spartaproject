#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/path/path_handle.sh

_add_path_identifier() (
    declare -r _identifier="XXXXXXXX"
    declare -r _path_head="$1"

    echo "${_path_head}#${_identifier}"
)

#*  Args:
#*      $1 (string):
#*          Path of the sub-directory where temporary file is generated.
#*
#*      $2 (string):
#*          The file name which will be suffixed with a random string.
#*
#*      $3 (string): The suffix for the temporary file.
#*
#*  Return:
#*      (string): Path of the temporary file which was created.
#*
get_temporary_file() (
    declare -r _group_root="$1"
    declare -r _path_head="$2"
    declare -r _suffix="$3"

    declare -r _temporary=$(begin_temporary_root "${_group_root}")
    declare -r _name=$(_add_path_identifier "${_path_head}")

    mktemp --tmpdir="${_temporary}" --suffix=".${_suffix}" "${_name}"
)

#*  Args:
#*      $1 (string):
#*          Path of the sub-directory where temporary directory is generated.
#*
#*      $2 (string):
#*          The directory name which will be suffixed with a random string.
#*
#*  Return:
#*      (string): Path of the temporary directory created.
#*
get_temporary_directory() (
    declare -r _group_root="$1"
    declare -r _path_head="$2"

    declare -r _temporary=$(begin_temporary_root "${_group_root}")
    declare -r _name=$(_add_path_identifier "${_path_head}")

    mktemp --directory --tmpdir="${_temporary}" "${_name}"
)
