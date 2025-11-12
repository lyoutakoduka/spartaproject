#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

get_package_root() (
    declare -r _package_base=$(constant::package_base)
    declare -r _package_main=$(constant::package_main)
    declare -r _package_script=$(constant::package_script)
    declare -r _package_sub=$(constant::package_sub)

    _get_root_main() {
        echo "${_package_base}/${_package_main}"
    }

    _get_root_sub() {
        echo "${_package_script}/${_package_sub}"
    }

    _main() {
        declare -r root_main=$(_get_root_main)
        declare -r root_sub=$(_get_root_sub)

        echo "${root_main}/${root_sub}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
