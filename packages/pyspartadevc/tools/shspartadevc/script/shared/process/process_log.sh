#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/get_file_path.sh
. packages/pyspartadevc/tools/shspartadevc/script/shared/show_message.sh

show_preprocess_log() (
    declare -r _group="$1"

    declare -r _path=$(shell::get_file_path)

    show_log "${_group}: ${_path}"
)
