#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show_message.sh

_set_environment() (
    declare -r _quote="\""
    declare -r _command="export"
    declare -r _key="$1"
    declare -r _value="$2"

    _create_environment() {
        declare -r quote_added=$(string_quoted "${_value}" "${_quote}")
        export_lines "${_command} ${_key}=${quote_added}"
    }

    _main() {
        if [[ -n "${_key}" ]] && [[ -n "${_value}" ]]; then
            _create_environment
        fi
    }

    _main
)

_add_environment_variable() (
    declare -r _name_key=$(constant::name_key)
    declare -r _user_key=$(constant::user_key)
    declare -r _identifier_key=$(constant::group_key)

    _set_user_name() {
        declare -r _user_name=$(whoami)
        _set_environment "${_name_key}" "${_user_name}"
    }

    _set_user_identifier() {
        declare -r _user_value=$(id --user)
        _set_environment "${_user_key}" "${_user_value}"
    }

    _set_group_identifier() {
        declare -r identifier=$(id --group)
        _set_environment "${_identifier_key}" "${identifier}"
    }

    _main() {
        _set_user_name
        _set_user_identifier
        _set_group_identifier
    }

    _main
)

ready_identifier() (
    declare -r -i _expected=$(constant::expected_identifier)
    declare -r _identifier=$(constant::message_identifier)
    declare -r _comment=$(constant::header_environment)

    _set_user_information() {
        show_log "${_identifier}"
        export_lines "${_comment}"

        _add_environment_variable

    }

    _main() {
        declare -r identifier=$(id --user)

        if [[ "${identifier}" -ne "${_expected}" ]]; then
            _set_user_information
        fi
    }

    _main
)
