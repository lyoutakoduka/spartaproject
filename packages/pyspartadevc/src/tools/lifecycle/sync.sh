#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

change_own() {
    name="$(whoami)"
    sudo chown "$name":"$name" "$1"
}
