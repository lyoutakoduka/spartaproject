export PATH=$HOME/develop/external/dropbox/.dropbox-dist/dropbox-lnx.x86_64-183.4.7058:$PATH
export PATH=$HOME/develop/external/pyenv/bin:$PATH
export PATH=$HOME/.local/bin:$PATH
export PATH=/usr/local/bin:$PATH
export PYENV_ROOT=$HOME/develop/external/pyenv:$PYENV_ROOT
export PS1="\n"$PS1

alias python='python3.11'
python ~/develop/external/dropbox/dropbox.py start
cd ~/develop/project/spartaproject
