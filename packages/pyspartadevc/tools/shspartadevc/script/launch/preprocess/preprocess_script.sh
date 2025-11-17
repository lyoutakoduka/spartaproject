#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/launch/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_body.sh
. packages/pyspartadevc/tools/shspartadevc/script/launch/preprocess/preprocess_head.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/set_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_end.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/path/path_temporary.sh

create_preprocess_script() (
    declare -r _group="$1"
    declare -r _empty=$(constant::empty)
    declare -r _expected=$(constant::group_create)
    declare -r _script_create=$(constant::script_create)
    declare -r _script_attach=$(constant::script_attach)

    _get_preprocess() {
        declare path="${_empty}"

        if [[ "${_group}" = "${_expected}" ]]; then
            path=$(get_preprocess_script "${_script_create}")
        else
            path=$(get_preprocess_script "${_script_attach}")
        fi

        echo "${path}"
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
