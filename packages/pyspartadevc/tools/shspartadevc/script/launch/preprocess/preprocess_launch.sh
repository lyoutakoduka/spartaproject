#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/account/account_filter.sh.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_invalid.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_select.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_script.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_message.sh

preprocess_launch() (
    declare -r _create="create"
    declare -r _attach="attach"
    declare -r _separator=","
    declare -r _arguments=("$@")
    declare -r _message=$(constant::help_launch)

    _filter_by_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        filter_by_invalid "${invalid}" || exit 1
        filter_by_help "${help}" "${_message}" || exit 1
    }

    _handle_arguments() {
        declare -r flags=$(select_arguments "${_arguments[@]}")

        declare help invalid
        IFS="${_separator}" read -r help invalid <<<"${flags}"

        _filter_by_arguments "${help}" "${invalid}"
    }

    _create_preprocess_scripts() {
        declare -r _groups=("$@")

        for group in "${_groups[@]}"; do
            create_preprocess_script "${group}"
        done
    }

    _main() {
        _handle_arguments
        filter_by_account || exit 1
        _create_preprocess_scripts "${_create}" "${_attach}"
    }

    _main
)
