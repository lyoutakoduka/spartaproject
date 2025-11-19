#!/bin/bash

constant::config() {
    echo ".devcontainer/devcontainer.json"
}

constant::config_main() {
    echo ".devcontainer"
}

constant::config_sub() {
    echo "devcontainer.json"
}

constant::current() {
    echo "."
}
