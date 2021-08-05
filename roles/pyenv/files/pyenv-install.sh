#!/bin/bash
# installs pyenv in userspace
cd
curl https://pyenv.run | bash
#
cp ~/.profile ~/.profile.old
cat /dev/stdin ~/.profile.old >~/.profile <<'INPUTEND1'
# added by runonce as pyenv config, must precede source .bashrc:
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
#
INPUTEND1
#
rm ~/.profile.old
cat >>~/.bashrc <<'INPUTEND2'
# added by runonce as pyenv config
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
INPUTEND2

