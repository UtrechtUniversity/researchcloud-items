#!/bin/bash install python module poetry
#
echo "Installing Python poetry"
curl -sSL https://install.python-poetry.org | python3 -
export POETRY_ROOT="~/.poetry"
export PATH="$POETRY_ROOT/bin:$PATH"
poetry self update
#
cat >> ~/.bashrc <<'INPUTEND'
# added by runonce as poetry config
if [ -z "$POETRY_ROOT" ]; then
export POETRY_ROOT="~/.poetry"
export PATH="$POETRY_ROOT/bin:$PATH"
fi
INPUTEND
