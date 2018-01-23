#!/usr/bin/env bash

sudo apt-get update

# Install Python
mkdir setup && cd setup
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b
export PATH="$HOME/miniconda3/bin:$PATH"
source ~/.bashrc

# Install dependencies
sudo apt-get install libgtk2.0-0 -y
conda install -y -c menpo opencv3
conda install -y numba cython
pip install pynput tweepy imageio

# Get the project code
cd ..
wget https://github.com/alvaropp/interactive-fluid-twitter/archive/master.zip
sudo apt-get install unzip
unzip master.zip
cd interactive-fluid-twitter-master/csim
python setup.py build_ext --inplace
cd ..
mkdir server && cd server
mkdir in && mkfir out
cd ..
python serve.py
