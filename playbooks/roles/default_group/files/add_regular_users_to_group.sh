#!/bin/bash
set -euo pipefail

# Require group name as $1
if [ $# -lt 1 ] || [ -z "$1" ]; then
    echo "Usage: $0 <groupname>" >&2
    exit 1
fi

TARGET_GROUP="$1"

# Ensure group exists
if ! getent group "$TARGET_GROUP" >/dev/null; then
    echo "Group $TARGET_GROUP does not exist" >&2
    exit 1
fi

for homedir in /home/*; do
    # Skip non-directories
    [ -d "$homedir" ] || continue

    user="$(basename "$homedir")"

    # Skip if user does not exist
    if ! id "$user" >/dev/null 2>&1; then
        continue
    fi

    # Add user to group if not already a member
    if ! id -nG "$user" | grep -qw "$TARGET_GROUP"; then
        usermod -aG "$TARGET_GROUP" "$user"
        echo "Added $user to $TARGET_GROUP"
    fi
done