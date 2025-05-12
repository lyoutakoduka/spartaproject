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


        -p  Identifier for development project.
            Type: string
            Default: pyspartadevc
            Proposal: [pyspartadevc|pyspartalib|pyspartaimg]

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
    local project="pyspartadevc"
    local attach=""
    local help=""
    local invalid=""

    while getopts "g:p:h" opt; do
        case "$opt" in
            g)
                group="$OPTARG"
                ;;
            p)
                project="${OPTARG}"
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

    echo ""$group","$project","$help","$invalid""
}
