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
