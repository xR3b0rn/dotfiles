#!/bin/bash

pwn=$(dirname -- "${0}")
echo ${pwn}
ln -s $(cd . && pwd)/.zshrc ${HOME}/.
ln -s $(cd . && pwd)/.tmux.conf ${HOME}/.
