#!/bin/bash

constant::identifier_expected() {
    echo 1000
}

constant::empty() {
    echo ""
}

constant::separator() {
    echo ","
}

constant::enter() {
    echo " \\"
}

constant::quote() {
    echo "\""
}

constant::status_success() {
    echo "true"
}

constant::status_fail() {
    echo "false"
}

constant::group_create() {
    echo "create"
}

constant::group_attach() {
    echo "attach"
}

constant::root() {
    echo "root"
}
