#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/path/path_package.sh

get_command_config() (
    declare -r _flag_config="--config"
    declare -r _config_path=$(constant::config)
    declare -r _indent=$(constant::indent)

    declare -r _package_root=$(get_package_root)
    declare -r config_path="${_package_root}/${_config_path}"

    echo "${_indent}${_flag_config} ${config_path}"
)
