#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

get_command_config() (
    declare -r _flag_config="--config"
    declare -r _config_path=$(constant::config)
    declare -r _indent=$(constant::indent)

    echo "${_indent}${_flag_config} ${_config_path}"
)
