#!/bin/bash

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
