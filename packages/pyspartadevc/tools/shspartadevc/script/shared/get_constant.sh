#!/bin/bash

constant::expected_identifier() {
    declare -g FFB275B
    if [[ "${FFB275B}" == "true" ]]; then
        echo 1234
    else
        echo 1000
    fi
}

constant::expected_name() {
    declare -g FFB275C
    if [[ "${FFB275C}" == "true" ]]; then
        echo "other"
    else
        echo "root"
    fi
}

constant::package_main() {
    echo "pyspartadevc"
}

constant::enter() {
    echo " \\"
}

constant::indent() {
    echo "    "
}

constant::group_text_remove() {
    echo "Remove"
}

constant::group_text_create() {
    echo "Create"
}

constant::name_key() {
    echo "DEVC_USER"
}

constant::user_key() {
    echo "DEVC_UID"
}

constant::group_key() {
    echo "DEVC_GID"
}

constant::config() {
    echo "packages/pyspartadevc/tools/shspartadevc/.devcontainer/devcontainer.json"
}

constant::temporary_create() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_create.sh"
}

constant::temporary_attach() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_attach.sh"
}

constant::temporary_post() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_post.sh"
}

constant::volume_cache() {
    echo ".temp/cache"
}

constant::volume_python() {
    echo ".venv"
}

constant::volume_javascript() {
    echo "node_modules"
}

constant::current() {
    echo "."
}

constant::header_post() {
    echo "# * Execute this script that finalize to create the dev-container."
}

constant::header_create() {
    echo "# * Execute this script that create a dev-container."
}

constant::header_attach() {
    echo "# * Execute this script that attach to the dev-container."
}

constant::comment_owner() {
    echo "# Change directory owner to non-root user."
}

constant::comment_sync() {
    echo "# Sync the package managers."
}

constant::header_environment() {
    echo "# Set environment variables."
}

constant::header_devcontainer() {
    echo "# Handle the dev-container."
}

constant::message_user() {
    echo "Executed by the root user."
}

constant::message_identifier() {
    echo "Executed by the none-default user."
}

constant::help_launch() {
    echo "Create the script that create a dev-container."
}

constant::help_attach() {
    echo 'Launched the terminal "zsh".'
}

constant::message_invalid() {
    echo 'Invalid option. See help "-h"'
}

constant::help_header() {
    echo "Usage: command [<options>...]"
}

constant::help_help() {
    mapfile str <<EOF
Usage: command [<options>...]

    Create the script that create a dev-container.

    Options:
        -h  Show help
            Type: boolean
            Default: false
EOF
    echo "${str[@]}"
}
