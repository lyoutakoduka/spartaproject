#!/bin/bash

change_owner() {
    local name="$(whoami)"
    sudo chown "$name":"$name" "$1"
}

change_path_owner() {
    show_log "Change directory owner to non-root user."

    local paths=(".temp/cache" ".venv" "node_modules")

    for path in "${paths[@]}"; do
        change_owner "$path"
    done
}
