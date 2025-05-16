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

set_user() {
    local identifier="$(id --user)"

    local user_name=""
    local user_identifier=""
    local group_identifier=""

    if [ "$identifier" -ne 1000 ]; then
        show_log "Executed by the none-default user."

        user_name="$(whoami)"
        user_identifier="$identifier"
        group_identifier="$(id --group)"
    fi

    set_environment "DEVC_USER" "$user_name"
    set_environment "DEVC_UID" "$user_identifier"
    set_environment "DEVC_GID" "$group_identifier"
}
