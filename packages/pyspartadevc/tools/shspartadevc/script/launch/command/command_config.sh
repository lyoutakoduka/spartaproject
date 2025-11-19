#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_command.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/path/path_package.sh

get_command_config() (
    declare -r _config_main=".devcontainer"
    declare -r _config_sub="devcontainer.json"
    declare -r _flag_config="--config"
    declare -r _config_path=$(constant::config)
    declare -r _indent=$(constant::indent)

    _get_config_path() {
        declare -r _package_root=$(get_package_root)

        echo "${_package_root}/${_config_path}"
    }

    _get_config() {
        declare -r config_path=$(_get_config_path)

        echo "${_flag_config} ${config_path}"
    }

    _main() {
        declare -r config=$(_get_config)

        echo "${_indent}${config}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
