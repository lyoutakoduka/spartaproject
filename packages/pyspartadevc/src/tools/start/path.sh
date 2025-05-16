#!/bin/bash

root="$(dirname "$0")"

get_config() {
    local project="$(get_environment "DEVC_PROJECT")"
    local config=".devcontainer/devcontainer.json"

    echo ""$root"/../../../"$project"/"$config""
}
