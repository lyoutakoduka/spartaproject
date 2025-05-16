#!/bin/bash

root="$(dirname "$0")"

source "$root/lifecycle/after.sh"

main() {
    local group="$1"

    if [ "$group" = "create" ]; then
        after_create
    elif [ "$group" = "attach" ]; then
        after_attach
    fi
}

main "$@"
