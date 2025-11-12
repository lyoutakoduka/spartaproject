#!/bin/bash

constant::header_post() {
    echo "# * Execute this script that finalize to create the dev-container."
}

constant::comment_owner() {
    echo "# Change directory owner to non-root user."
}

constant::comment_sync() {
    echo "# Sync the package managers."
}
