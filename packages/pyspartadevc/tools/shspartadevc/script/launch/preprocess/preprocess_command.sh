#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh

get_command_exists() (
    declare -r _flag_exists="--remove-existing-container"
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    echo "${_indent}${_flag_exists}${_enter}"
)

get_command_devcontainer() (
    declare -r command_base="devcontainer up"
    declare -r _enter=$(constant::enter)

    echo "${command_base}${_enter}"
)

get_command_workspace() (
    declare -r _flag_workspace="--workspace-folder"
    declare -r _current=$(constant::current)
    declare -r _indent=$(constant::indent)
    declare -r _enter=$(constant::enter)

    declare -r workspace="${_flag_workspace} ${_current}"
    echo "${_indent}${workspace}${_enter}"
)

get_command_config() (
    declare -r _flag_config="--config"
    declare -r _config_path=$(constant::config)
    declare -r _indent=$(constant::indent)

    echo "${_indent}${_flag_config} ${_config_path}"
)
