#!/bin/bash

constant::message_invalid() {
    echo 'Invalid option. See help "-h"'
}

constant::help_header() {
    echo "Usage: command [<options>...]"
}

constant::help_help() {
    mapfile str <<EOF
    Options:
        -h  Show help
            Type: boolean
            Default: false
EOF
    echo "${str[@]}"
}
