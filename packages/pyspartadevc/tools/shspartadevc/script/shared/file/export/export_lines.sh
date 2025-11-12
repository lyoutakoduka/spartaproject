#!/bin/bash

. packages/pyspartadevc/tools/shspartadevc/script/shared/file/export/export_line.sh

export_lines() (
    _main() {
        for text in "$@"; do
            export_line "${text}"
        done
    }

    _main "$@"
)
