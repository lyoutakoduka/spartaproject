#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

usage() {
    cat <<EOF
Usage: command [<options>...]

    Options:
        -c  Create devcontainer
            Type: boolean
            Default: false

        -a  Attach to devcontainer
            Type: boolean
            Default: false

        -h  Show help
            Type: boolean
            Default: false

EOF
}

usage_error() {
    show_error 'Invalid option. See help "-h"'
    usage
}
