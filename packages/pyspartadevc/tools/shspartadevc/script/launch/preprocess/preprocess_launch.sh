#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_filter.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_invalid.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_select.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_script.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh

_handling_arguments() (
    declare -r _separator=","
    declare -r _arguments=("$@")

    _filter_by_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        filter_by_invalid "${invalid}" || exit 1
        filter_by_help "${help}" || exit 1
    }

    _main() {
        declare -r flags=$(select_arguments "${_arguments[@]}")

        declare help invalid
        IFS="${_separator}" read -r help invalid <<<"${flags}"

        _filter_by_arguments "${help}" "${invalid}"
    }

    _main
)

preprocess_launch() (
    declare -r _create="create"
    declare -r _attach="attach"
    declare -r _arguments=("$@")

    _main() {
        _handling_arguments "${_arguments[@]}" || exit 1
        filter_by_account || exit 1

        create_preprocess_script "${_create}"
        create_preprocess_script "${_attach}"
    }

    _main
)
