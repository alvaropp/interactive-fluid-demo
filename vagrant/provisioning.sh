#!/usr/bin/env bash

# Install miniconda Python
cd /vagrant
wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b -p /opt/anaconda
export PATH=/opt/anaconda/bin:$PATH
echo 'export PATH=/opt/anaconda/bin:$PATH' >> /home/vagrant/.bashrc
echo "============================= Finished installing miniconda ============================"

# Install dependencies
sudo apt-get install libgtk2.0-0 -y
sudo apt-get install gcc -y
conda install -y -c menpo opencv3
# pip install opencv-python
conda install -y numba cython twython slackclient
pip install pynput imageio
echo "============== Finished installing interactive-fluid-twitter dependencies =============="

# Get the project code
cd /home/vagrant/
wget https://github.com/alvaropp/interactive-fluid-twitter/archive/master.zip
sudo apt-get install unzip
unzip master.zip
cd interactive-fluid-twitter-master/csim
python setup.py build_ext --inplace
cd .. && mkdir server && cd server
mkdir in && mkdir out && cd ..
mv ../credentials.txt ./
chown -R vagrant:vagrant ../interactive-fluid-twitter-master/
echo "============== Finished installing interactive-fluid-twitter =============="
