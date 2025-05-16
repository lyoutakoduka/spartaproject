#!/bin/bash

root="$(dirname "$0")"

source "$root/start/argument.sh"
source "$root/start/devcontainer.sh"
source "$root/share/environment.sh"
source "$root/start/user.sh"

select_invalid() {
    usage_error
    exit 1
}

select_help() {
    usage
    exit 0
}

shared_process() {
    set_environment "DEVC_PROJECT" "$1"
    filter_root
}

select_create() {
    set_user
    create_devcontainer
}

select_attach() {
    attach_devcontainer
}
