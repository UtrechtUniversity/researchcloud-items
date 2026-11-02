#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# this command will return the .add_info[0].local attribute of any interface that matches a local network ip4
# this ip could be either the ip4 or ip6 address -- we don't much care which we use.
result=$(ip -j addr | jq -r '.[] | select(.addr_info[]?.local | test("^(10\\.|172\\.(1[6-9]|2[0-9]|3[0-1])\\.|192\\.168\\.)")) | .addr_info[0].local')

if [[ -z "$result" ]]; then
    echo "No private network found"
    exit 1
fi

echo $result