#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_invalid.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/arguments/arguments_select.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_help.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/handle_account.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_script.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_message.sh

launch_preprocess() (
    declare -r _message=$(constant::help_launch)
    declare -r _create=$(constant::group_create)
    declare -r _attach=$(constant::group_attach)
    declare -r _separator=$(constant::separator)

    _exit() {
        exit 1
    }

    _filter_by_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        filter_by_invalid "${invalid}" || exit 1
        filter_by_help "${help}" "${_message}" || exit 1
    }

    _handle_arguments() {
        declare -r arguments=$(select_arguments "$@")

        declare help invalid
        IFS="${_separator}" read -r help invalid <<<"${arguments}"

        _filter_by_arguments "${help}" "${invalid}"
    }

    _create_preprocess_scripts() {
        for item in "$@"; do
            create_preprocess_script "${item}"
        done
    }

    _main() {
        _handle_arguments "$@"
        filter_by_account || exit 1
        _create_preprocess_scripts "${_create}" "${_attach}"
    }

    _main "$@"
)
