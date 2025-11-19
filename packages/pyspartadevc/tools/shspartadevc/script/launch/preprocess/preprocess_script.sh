#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_body.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_head.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/set_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_end.sh

create_preprocess_script() (
    declare -r _expected="create"
    declare -r _group="$1"
    declare -r _script_create=$(constant::temporary_create)
    declare -r _script_attach=$(constant::temporary_attach)

    _get_preprocess() {
        if [[ "${_group}" = "${_expected}" ]]; then
            echo "${_script_create}"
        else
            echo "${_script_attach}"
        fi
    }

    _whole_text_file() {
        begin_text_file

        head_text_file "${_group}"
        body_text_file "${_group}"

        end_text_file
    }

    _main() {
        declare -r path=$(_get_preprocess)
        shell::set_file_path "${path}"

        _whole_text_file
    }

    _main
)
