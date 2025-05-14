#!/bin/bash

root="$(dirname "$0")"

source "$root/start/argument.sh"
source "$root/start/select.sh"

main() {
    local result="$(select_arguments "$@")"

    local group project help invalid
    IFS=',' read -r group project help invalid <<<"$result"

    if [ "$invalid" = "true" ]; then
        select_invalid
    fi

    if [ "$help" = "true" ]; then
        select_help
    fi

    shared_process "$project"

    if [ "$group" = "create" ]; then
        select_create
    elif [ "$group" = "attach" ]; then
        select_attach
    fi
}

main "$@"
