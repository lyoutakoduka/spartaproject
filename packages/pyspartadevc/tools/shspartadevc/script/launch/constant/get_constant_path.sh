#!/bin/bash

constant::config() {
    echo "packages/pyspartadevc/tools/shspartadevc/.devcontainer/devcontainer.json"
}

constant::current() {
    echo "."
}

constant::temporary_create() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_create.sh"
}

constant::temporary_attach() {
    echo "packages/pyspartadevc/tools/shspartadevc/.temp/devcontainer_attach.sh"
}
