#!/bin/bash

root="$(dirname "$0")"

source "$root/share/log.sh"

set_environment() {
  local key="$1"
  local value="$2"

  if [ -n "$key" ] && [ -n "$value" ]; then
    show_log "Set environment variables: "$key""
    export "$key"="$value"
  fi
}

get_environment() {
  local key="$1"

  if [[ -v "$key" ]]; then
    echo "${!key}"
  else
    echo "false"
  fi
}
