#!/bin/bash

get_selected_frame() (
    declare -r -i _depth=3
    declare -r -i _index_default=0
    declare -r _group="$1"
    declare _index_any="$2"

    _get_stack_frame() {
        declare -r -i index="$1"

        if [[ "${_group}" = "path" ]]; then
            echo "${BASH_SOURCE[index]}"
        else
            echo "${FUNCNAME[index]}"
        fi
    }

    _update_offset() {
        if [[ -z "${_index_any}" ]]; then
            echo "${_index_default}"
        else
            echo "${_index_any}"
        fi
    }

    _main() {
        declare -r -i offset=$(_update_offset)
        declare -r -i index=$((offset + _depth))

        _get_stack_frame "${index}"
    }

    _main
)
