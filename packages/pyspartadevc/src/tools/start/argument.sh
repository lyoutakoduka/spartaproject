#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

usage() {
    cat <<EOF
Usage: command [<options>...]

    Options:
        -g  Operation group for dev-container.
            Type: string
            Default: create
            Proposal: [create|attach]

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
}

select_arguments() {
    local group="create"
    local create=""
    local attach=""
    local help=""
    local invalid=""

    while getopts "g:cah" opt; do
        case "$opt" in
            g)
                group="$OPTARG"
                ;;
            c)
                create="true"
                ;;
            a)
                attach="true"
                ;;
            h)
                help="true"
                ;;
            \?)
                invalid="true"
                ;;
        esac
    done

    shift $((OPTIND - 1))

    echo "$group,$create,$attach,$help,$invalid"
}
