#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_environment.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh

set_group_identifier() (
    declare -r _identifier_key=$(constant::group_key)

    declare -r identifier=$(id --group)
    set_environment "${_identifier_key}" "${identifier}"
)
