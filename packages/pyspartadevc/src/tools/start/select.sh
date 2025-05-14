#!/bin/bash

root="$(dirname "$0")"

source "$root/start/user.sh"

select_invalid() {
    usage_error
    exit 1
}

select_help() {
    usage
    exit 0
}
