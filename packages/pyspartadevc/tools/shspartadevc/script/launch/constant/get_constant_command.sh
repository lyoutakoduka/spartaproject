#!/bin/bash

constant::devcontainer_main() {
    echo "devcontainer"
}

constant::devcontainer_sub() {
    echo "up"
}

constant::flag_workspace() {
    echo "--workspace-folder"
}

constant::flag_config() {
    echo "--config"
}

constant::flag_exists() {
    echo "--remove-existing-container"
}

constant::identifier_user() {
    echo "--user"
}

constant::identifier_group() {
    echo "--group"
}

constant::environment() {
    echo "export"
}
