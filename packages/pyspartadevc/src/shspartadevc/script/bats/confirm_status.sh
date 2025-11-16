#!/usr/bin/env bats

shell::confirm_success() {
    declare -r -i _status=$1

    [[ ${_status} -eq 0 ]]
}

shell::confirm_error() {
    declare -r -i _status=$1

    [[ ${_status} -eq 1 ]]
}
