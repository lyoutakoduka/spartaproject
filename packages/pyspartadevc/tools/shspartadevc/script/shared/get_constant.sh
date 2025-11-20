#!/bin/bash

constant::package_main() {
    echo "pyspartadevc"
}

constant::indent() {
    echo "    "
}

constant::group_text_remove() {
    echo "Remove"
}

constant::group_text_create() {
    echo "Create"
}

constant::volume_cache() {
    echo ".temp/cache"
}

constant::volume_python() {
    echo ".venv"
}

constant::volume_javascript() {
    echo "node_modules"
}

constant::temporary_post() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_post.sh"
}

constant::header_post() {
    echo "# * Execute this script that finalize to create the dev-container."
}

constant::comment_owner() {
    echo "# Change directory owner to non-root user."
}

constant::comment_sync() {
    echo "# Sync the package managers."
}

constant::help_attach() {
    echo 'Launched the terminal "zsh".'
}
