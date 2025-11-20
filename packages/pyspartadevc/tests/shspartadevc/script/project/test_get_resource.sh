#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/error/error_difference.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_resource.sh
. packages/pyspartadevc/src/shspartadevc/script/project/get_stack_trace.sh

_get_resource_root() (
    declare -r _root_main="packages/pyspartadevc"
    declare -r _root_sub="tests/shspartadevc"
    declare -r _resource="script/project/resource"

    echo "${_root_main}/${_root_sub}/${_resource}"
)

_get_executed_path() (
    declare -r _group="path"
    get_selected_frame "${_group}"
)

test_base() {
    declare -r executed_path=$(_get_executed_path)
    declare -r result=$(get_resource "${executed_path}")
    declare -r resource_root=$(_get_resource_root)

    shell::error_difference "${result}" "${resource_root}"
}

test_local() {
    declare -r _local_path="root/head.json"

    _main() {
        declare -r executed_path=$(_get_executed_path)
        declare -r result=$(get_resource "${executed_path}" "${_local_path}")
        declare -r resource_root=$(_get_resource_root)

        shell::error_difference "${result}" "${resource_root}/${_local_path}"
    }

    _main
}

"$@"
