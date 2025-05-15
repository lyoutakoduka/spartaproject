#!/bin/bash

change_owner() {
    local name="$(whoami)"
    sudo chown "$name":"$name" "$1"
}
