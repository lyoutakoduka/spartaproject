#!/bin/bash

root="$(dirname "$0")"

source "$root/start/user.sh"

select_invalid() {
    usage_error
    exit 1
}
