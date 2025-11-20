#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess_launch.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/lifecycle/lifecycle_attach.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/lifecycle/lifecycle_create.sh

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
