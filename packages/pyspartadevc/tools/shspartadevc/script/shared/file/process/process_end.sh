#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant_message.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_head.sh

end_text_file() (
    declare -r _group=$(constant::group_text_create)

    _main() {
        declare -r path=$(get_file_path)

        if [[ -e "${path}" ]]; then
            show_preprocess_log "${_group}"
        fi
    }

    _main
)
