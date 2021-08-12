#!/bin/bash
# installs pyenv in userspace
cd
curl https://pyenv.run | bash
#
# add pyenv to .profile for future logins
#cp ~/.profile ~/.profile.old
#cat /dev/stdin ~/.profile.old >~/.profile <<'INPUTEND1'
# added by runonce as pyenv config, must precede source .bashrc:
#export PYENV_ROOT="$HOME/.pyenv"
#export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
#
#INPUTEND1
#
#rm ~/.profile.old
cat >>~/.bashrc <<'INPUTEND2'
# added by runonce as pyenv config
if [ -z "$PYENV_ROOT" ]; then
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"
fi
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
INPUTEND2
#
# also add pyenv to current login shell
#export PYENV_ROOT="$HOME/.pyenv"
#export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

