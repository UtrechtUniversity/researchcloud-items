#!/bin/bash
# installs pyenv in userspace
cd
curl https://pyenv.run | bash
#
# todo? pyenv recommends below cmds to be added to .profile
#       and be executed before ~/.bashrc is sourced
# 
#
cat >>~/.profile <<'INPUTEND1'
# added by runonce as pyenv config:
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
# load pyenv and pyenv-virtualenv automatically
INPUTEND1
cat >>~/.bashrc <<'INPUTEND2'
# added by runonce as pyenv config
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
INPUTEND2

