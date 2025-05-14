#!/bin/bash

root="$(dirname "$0")"

source "$root/start/path.sh"

get_shared_arguments() {
    local path="$(get_config)"

    local config="--config "$path""
    local workspace="--workspace-folder ."

    echo ""$config" "$workspace""
}
