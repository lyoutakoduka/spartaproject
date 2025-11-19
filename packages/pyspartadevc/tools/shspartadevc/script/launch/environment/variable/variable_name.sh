#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_name() (
    declare -r _name_key=$(constant::name_key)

    declare -r _user_name=$(whoami)
    set_environment "${_name_key}" "${_user_name}"
)
