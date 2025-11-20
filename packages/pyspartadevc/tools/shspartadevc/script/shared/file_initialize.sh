#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/export_line.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/get_constant.sh

initialize_text_file() (
    declare -r _header="$1"
    declare -r _shebang="#!/bin/bash"

    export_lines "${_shebang}" "${_header}"
)
