#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/constant/get_constant.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

initialize_text_file() (
    declare -r _header="$1"
    declare -r _shebang="#!/bin/bash"

    _main() {
        export_line "${_shebang}" "${_header}"
    }

    _main
)
