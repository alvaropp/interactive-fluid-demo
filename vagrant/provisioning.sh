#!/usr/bin/env bash
# set -e # Exit script immediately on first error.
set -x # Print commands and their arguments as they are executed.

# Install miniconda Python
cd /vagrant
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

chmod +x miniconda.sh
./miniconda.sh -b -p /opt/anaconda

# cat >> /home/vagrant/.bashrc << END
# PATH=/opt/anaconda/bin:\$PATH
# END
export PATH=/opt/anaconda/bin:$PATH

echo "============================= Finished installing miniconda ============================"

# Install dependencies
sudo apt-get install libgtk2.0-0 -y
sudo apt-get install gcc -y
conda install -y -c menpo opencv3
conda install -y numba cython
pip install pynput tweepy imageio
echo "============== Finished installing interactive-fluid-twitter dependencies =============="

# Get the project code
cd /home/vagrant/
echo =======================================
pwd
echo =======================================
wget https://github.com/alvaropp/interactive-fluid-twitter/archive/master.zip
sudo apt-get install unzip
unzip master.zip
chmod -R +xr interactive-fluid-twitter-master
cd interactive-fluid-twitter-master/csim
python setup.py build_ext --inplace
cd .. && mkdir server && cd server
mkdir in && mkdir out && cd ..
mv ../credentials.txt ./
echo "============== Finished installing interactive-fluid-twitter =============="

python serve.py
