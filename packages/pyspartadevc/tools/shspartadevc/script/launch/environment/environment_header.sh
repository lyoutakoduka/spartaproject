#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

environment_comment() (
    declare -r _comment=$(constant::header_environment)

    export_line "${_comment}"
)
