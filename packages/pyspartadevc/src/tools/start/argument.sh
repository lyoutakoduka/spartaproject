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

select_arguments() {
    local create=""
    local attach=""
    local help=""
    local invalid=""

    while getopts "cah" opt; do
        case "$opt" in
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

    echo "$create,$attach,$help,$invalid"
}
