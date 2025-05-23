#!/bin/bash

show_base() {
    echo "[pyspratadev:"$(whoami)":"$1"] "$2""
}

show_log() {
    show_base "log" "$1"
}

show_error() {
    show_base "error" "$1"
}

show_begin() {
    show_base "begin" "$1"
}

show_end() {
    show_base "end"
}
