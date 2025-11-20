#!/bin/bash

. packages/pyspartadevc/src/shspartadevc/script/string/string_quoted.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/shared_launch.sh

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

_ready_identifier() (
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

_add_text_file_launch() (
    declare -r _expected="create"
    declare -r _command_base="devcontainer up"
    declare -r _flag_exists="--remove-existing-container"
    declare -r _flag_config="--config"
    declare -r _flag_workspace="--workspace-folder"
    declare -r _group="$1"
    declare -r _message=$(constant::header_devcontainer)
    declare -r _enter=$(constant::enter)
    declare -r _indent=$(constant::indent)
    declare -r _config_path=$(constant::config)
    declare -r _current=$(constant::current)

    _add_command_head() {
        declare -r command="${_command_base}${_enter}"
        export_lines "${command}"
    }

    _add_command_body() {
        declare -r command="${_indent}${_flag_exists}${_enter}"
        export_lines "${command}"
    }

    _add_command_foot() {
        declare -r workspace="${_flag_workspace} ${_current}"
        declare -r command_workspace="${_indent}${workspace}${_enter}"
        declare -r command_config="${_indent}${_flag_config} ${_config_path}"

        export_lines "${command_workspace}" "${command_config}"
    }

    _add_command_base() {
        _add_command_head

        if [[ "${_group}" = "${_expected}" ]]; then
            _add_command_body "${_group}"
        fi

        _add_command_foot
    }

    _main() {
        _ready_identifier
        export_lines "${_message}"
        _add_command_base
    }

    _main
)

_create_preprocess_script() (
    declare -r _expected="create"
    declare -r _group="$1"
    declare -r _script_create=$(constant::temporary_create)
    declare -r _script_attach=$(constant::temporary_attach)
    declare -r _header_create=$(constant::header_create)
    declare -r _header_attach=$(constant::header_attach)

    _get_preprocess() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_script_create}"
        else
            echo "${_script_attach}"
        fi
    }

    _get_header() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_header_create}"
        else
            echo "${_header_attach}"
        fi
    }

    _whole_text_file() {
        begin_text_file

        declare -r header=$(_get_header)
        initialize_text_file "${header}"
        _add_text_file_launch "${_group}"

        end_text_file
    }

    _main() {
        declare -r path=$(_get_preprocess)
        shell::set_file_path "${path}"

        _whole_text_file
    }

    _main_#FF_0000_TOP() {
        shell::begin_text_file_#FF_0000_TOP

        declare -r header=$(_get_header)
        initialize_text_file "${header}"
        _add_text_file_launch "${_group}"

        declare -r script_path=$(_get_preprocess)
        end_text_file_#FF_0000_TOP "${script_path}"
    }

    declare -g FF_0000_TOP
    if [[ "${FF_0000_TOP}" = "true" ]]; then
        _main_#FF_0000_TOP
    else
        _main
    fi
)

_select_arguments() (
    declare -r _success="true"
    declare -r _fail="false"

    _shift_arguments() {
        shift $((OPTIND - 1))
    }

    _main() {
        declare help="${_fail}"
        declare invalid="${_fail}"

        declare opt
        while getopts "h" opt; do
            case "${opt}" in
            h)
                help="${_success}"
                ;;
            \?)
                invalid="${_success}"
                ;;
            *) ;;
            esac
        done

        _shift_arguments

        echo "${help},${invalid}"
    }

    _main "$@"
)

_handling_arguments() (
    declare -r _expected="true"
    declare -r _arguments=("$@")
    declare -r _message_invalid=$(constant::message_invalid)
    declare -r _message_help=$(constant::help_help)

    _filter_by_invalid() {
        declare -r invalid="$1"

        if [[ "${invalid}" = "${_expected}" ]]; then
            shell::show_warning "${_message_invalid}"
        fi
    }

    _filter_by_help() {
        declare -r help="$1"

        if [[ "${help}" = "${_expected}" ]]; then
            echo "${_message_help}"
            exit 1
        fi
    }

    _filter_by_arguments() {
        declare -r help="$1"
        declare -r invalid="$2"

        _filter_by_invalid "${invalid}" || exit 1
        _filter_by_help "${help}" || exit 1
    }

    _main() {
        declare -r flags=$(_select_arguments "${_arguments[@]}")

        declare help invalid
        IFS="," read -r help invalid <<<"${flags}"

        _filter_by_arguments "${help}" "${invalid}"
    }

    _main
)

preprocess_launch() (
    declare -r _create="create"
    declare -r _attach="attach"
    declare -r _arguments=("$@")
    declare -r _expected=$(constant::expected_name)
    declare -r _message=$(constant::message_user)

    _filter_by_account() {
        declare -r user_name=$(whoami)

        if [[ "${user_name}" = "${_expected}" ]]; then
            shell::show_warning "${_message}"
        fi
    }

    _main() {
        _handling_arguments "${_arguments[@]}" || exit 1
        _filter_by_account || exit 1

        _create_preprocess_script "${_create}"
        _create_preprocess_script "${_attach}"
    }

    _main
)
