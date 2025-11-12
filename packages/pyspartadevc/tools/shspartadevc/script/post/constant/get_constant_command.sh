#!/bin/bash

constant::change_main() {
    echo "sudo"
}

constant::change_sub() {
    echo "chown"
}

constant::sync_javascript() {
    echo "yarn"
}

constant::sync_python_main() {
    echo "uv"
}

constant::sync_python_sub() {
    echo "sync"
}

constant::terminal() {
    echo "zsh"
}
