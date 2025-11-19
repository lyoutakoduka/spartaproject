#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/post/command/command_owner.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/command/command_package.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_comment.sh
. packages/pyspartadevc/tools/shspartadevc/script/post/constant/get_constant_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/file_initialize.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/path/set_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_begin.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/process/process_end.sh

lifecycle_create() (
    declare -r _header=$(constant::header_post)
    declare -r _script_post=$(constant::temporary_post)

    _body_text_file() {
        create_command_owner
        command_package_manager
    }

    _whole_text_file() {
        begin_text_file

        initialize_text_file "${_header}"
        _body_text_file

        end_text_file
    }

    _main() {
        shell::set_file_path "${_script_post}"
        _whole_text_file
    }

    _main
)
