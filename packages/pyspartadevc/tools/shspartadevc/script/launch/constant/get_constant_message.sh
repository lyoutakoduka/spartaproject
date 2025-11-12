#!/bin/bash

constant::message_user() {
    echo "Executed by the root user."
}

constant::message_identifier() {
    echo "Executed by the none-default user."
}

constant::help_launch() {
    echo "Create the script that create a dev-container."
}
