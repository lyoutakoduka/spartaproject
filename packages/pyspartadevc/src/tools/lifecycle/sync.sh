#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

change_own() {
    name="$(whoami)"
    sudo chown "$name":"$name" "$1"
}

sync_yarn() {
    show_begin "Sync JavaScript package manager Yarn."

    change_own node_modules
    yarn

    show_end
}

sync_uv() {
    show_begin "Sync Python package manager UV."

    change_own .venv
    uv sync --group "$1"

    show_end
}
