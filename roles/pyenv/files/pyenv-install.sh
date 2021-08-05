#!/bin/bash
# installs pyenv in userspace
cd
curl https://pyenv.run | bash
#
# todo? pyenv recommends below cmds to be added to .profile
#       and be executed before ~/.bashrc is sourced
# 
#
cat >>~/.bashrc <<'INPUTEND'
# added by runonce as pyenv config:
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
# load pyenv and pyenv-virtualenv automatically
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
INPUTEND
# add pyenv to current login shell (to support immediate use in runonce scripts)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

