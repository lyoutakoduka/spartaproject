#!/bin/bash

root="$(dirname "$0")"

source "$root/share/environment.sh"
source "$root/lifecycle/sync.sh"

after_create() {
    sync_yarn
    sync_uv "$(get_environment "DEVC_PROJECT")"
}
