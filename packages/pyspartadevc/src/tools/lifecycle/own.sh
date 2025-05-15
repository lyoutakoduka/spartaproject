#!/bin/bash

change_own() {
    local name="$(whoami)"
    sudo chown "$name":"$name" "$1"
}
