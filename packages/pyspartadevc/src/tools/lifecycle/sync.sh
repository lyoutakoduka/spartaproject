#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

sync_yarn() {
    show_begin "Sync JavaScript package manager Yarn."
    yarn
    show_end
}

sync_uv() {
    show_begin "Sync Python package manager UV."
    uv sync --group "$1"
    show_end
}
