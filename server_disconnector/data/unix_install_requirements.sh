#!bin/bash

# show user su -
userTerminalLogin=`whoami`  # get user login
echo "[bash] connected as -> $userTerminalLogin"

echo "[bash] path -> $SHELL"  # show bash path

# install requirements
# upgrade pip for python3 
pip install --upgrade pip
pip3 install --upgrade pip3

# upgrade pip for python3
python install --upgrade pip
python install --upgrade pip3

# install for pip3
pip3 install os
pip install sys

# install for pip
pip install os
pip install sys

# show pkgs for pip
pip check os
pip check sys

# show pkgs for pip3
pip3 check os
pip3 check sys

# start disconnector again
python attack_file.py
python3 attack_file.py
