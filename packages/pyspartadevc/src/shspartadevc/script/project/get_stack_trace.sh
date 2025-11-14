#!/bin/bash

get_selected_frame() (
    declare -r -i _empty=""
    declare -r -i _depth=5
    declare -r -i _index_default=0
    declare -r _group="$1"
    declare _index_any="$2"

    _get_file_path() {
        declare -r -i index="$1"
        echo "${BASH_SOURCE[index]}"
    }

    _get_function_name() {
        declare -r -i index="$1"
        echo "${FUNCNAME[index]}"
    }

    _get_stack_frame() {
        declare -r -i index="$1"
        declare result="${_empty}"

        if [[ "${_group}" = "path" ]]; then
            result=$(_get_file_path "${index}")
        else
            result=$(_get_function_name "${index}")
        fi

        echo "${result}"
    }

    _get_stack_trace() {
        declare -r -i index="$1"

        declare -r result="$(_get_stack_frame "${index}")"
        echo "${result}"
    }

    _update_offset() {
        if [[ -z "${_index_any}" ]]; then
            echo "${_index_default}"
        else
            echo "${_index_any}"
        fi
    }

    _offset_index() {
        declare -r -i offset="$1"
        echo $((offset + _depth))
    }

    _get_index() {
        declare -r -i offset=$(_update_offset)
        declare -r -i index=$(_offset_index "${offset}")

        echo "${index}"
    }

    _main() {
        declare -r -i index=$(_get_index)
        declare -r result=$(_get_stack_trace "${index}")

        echo "${result}"
    }

    declare -r result=$(_main)
    echo "${result}"
)
