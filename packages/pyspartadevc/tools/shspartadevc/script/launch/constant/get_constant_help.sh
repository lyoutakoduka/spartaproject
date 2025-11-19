#!/bin/bash

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
