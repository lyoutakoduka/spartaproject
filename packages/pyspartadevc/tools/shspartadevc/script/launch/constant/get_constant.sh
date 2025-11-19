#!/bin/bash

constant::expected_identifier() {
    echo 1000
}

constant::enter() {
    echo " \\"
}

constant::expected_name() {
    echo "root"
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

constant::current() {
    echo "."
}

constant::header_create() {
    echo "# * Execute this script that create a dev-container."
}

constant::header_attach() {
    echo "# * Execute this script that attach to the dev-container."
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
