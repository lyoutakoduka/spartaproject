#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"
source "$root/share/environment.sh"

filter_root() {
    if [ "$(whoami)" = "root" ]; then
        show_error "Executed by the root user."
        exit 1
    fi
}
