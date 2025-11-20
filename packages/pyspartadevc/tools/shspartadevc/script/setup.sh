#!/bin/bash
readonly FF_0000_TOP="false"
readonly FF_0000_VER="false"

. packages/pyspartadevc/tools/shspartadevc/script/launch/lifecycle_attach.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/lifecycle_create.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess_launch.sh

_main() {
    declare -r _create="create"
    declare -r _attach="attach"
    declare -r _group="$1"
    declare -r _arguments=("$@")

    if [[ "${_group}" == "${_create}" ]]; then
        lifecycle_create
    elif [[ "${_group}" == "${_attach}" ]]; then
        lifecycle_attach
    else
        preprocess_launch "${_arguments[@]}"
    fi
}

_main "$@"
