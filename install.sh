#!/bin/bash

pwn=$(dirname -- "${0}")
ln -s $(cd . && pwd)/.taskrc ${HOME}
ln -s $(cd . && pwd)/.zshrc ${HOME}
ln -s $(cd . && pwd)/.tmux.conf ${HOME}
ln -s $(cd . && pwd)/.tmux ${HOME}
mkdir -p ${HOME}/.task
ln -s $(cd . && pwd)/.task/hooks ${HOME}/.task
mkdir -p ${HOME}/.config
ln -s $(cd . && pwd)/.config/timewarrior ${HOME}/.config/timewarrior
