#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"
source "$root/start/path.sh"

get_shared_arguments() {
    local path="$(get_config)"

    local config="--config "$path""
    local workspace="--workspace-folder ."

    echo ""$config" "$workspace""
}

create_devcontainer() {
    show_begin "Re-create the image and container."

    local arguments="$(get_shared_arguments)"
    local existing="--remove-existing-container"

    devcontainer up $existing $arguments

    show_end
}

attach_devcontainer() {
    show_begin "Attach to the container."

    local arguments="$(get_shared_arguments)"
    devcontainer up $arguments

    show_end
}
