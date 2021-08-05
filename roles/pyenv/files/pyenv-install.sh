#!/bin/bash
# installs pyenv in userspace
cd
curl https://pyenv.run | bash
#
cat >>~/.bashrc <<'INPUTEND'
# added by runonce as pyenv config:
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
INPUTEND

