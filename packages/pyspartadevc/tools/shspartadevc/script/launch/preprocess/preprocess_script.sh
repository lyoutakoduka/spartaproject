#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_body.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file_initialize.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/process/process_end.sh

create_preprocess_script() (
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
        add_text_file_launch "${_group}"

        end_text_file
    }

    _main() {
        declare -r path=$(_get_preprocess)
        shell::set_file_path "${path}"

        _whole_text_file
    }

    _main
)
