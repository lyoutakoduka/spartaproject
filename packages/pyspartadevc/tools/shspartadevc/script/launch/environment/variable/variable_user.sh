#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_user_identifier() (
    declare -r _user_key=$(constant::user_key)

    declare -r _user_value=$(id --user)
    set_environment "${_user_key}" "${_user_value}"
)
