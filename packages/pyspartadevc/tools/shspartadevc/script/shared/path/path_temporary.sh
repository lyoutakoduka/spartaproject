#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/path/path_package.sh

get_preprocess_script() (
    declare -r _script_name="$1"
    declare -r _temporary_root=".temp"

    _main() {
        declare -r package_root=$(get_package_root)
        echo "${package_root}/${_temporary_root}/${_script_name}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
