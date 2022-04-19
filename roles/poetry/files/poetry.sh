#!/bin/bash install python module poetry
#
echo "Installing Python poetry"
export POETRY_ROOT="~/.local/bin"
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$POETRY_ROOT/bin:$PATH"
#
cat >> ~/.bashrc <<'INPUTEND'
# added by runonce as poetry config
if [ -z "$POETRY_ROOT" ]; then
export POETRY_ROOT="~/.local/bin"
export PATH="$POETRY_ROOT:$PATH"
fi
INPUTEND
