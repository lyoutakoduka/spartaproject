#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/environment/environment_create.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show/show_message.sh

_add_environment_variable() (
    declare -r _name_key=$(constant::name_key)
    declare -r _user_key=$(constant::user_key)
    declare -r _identifier_key=$(constant::group_key)

    _set_user_name() {
        declare -r _user_name=$(whoami)
        set_environment "${_name_key}" "${_user_name}"
    }

    _set_user_identifier() {
        declare -r _user_value=$(id --user)
        set_environment "${_user_key}" "${_user_value}"
    }

    _set_group_identifier() {
        declare -r identifier=$(id --group)
        set_environment "${_identifier_key}" "${identifier}"
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
