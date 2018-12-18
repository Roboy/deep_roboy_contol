#!/usr/bin/env bash
# This file is for Ubuntu Xenial 16.04
# It installs:
# CUDA 9.0
# cuDNN 7.0
# Python 3.6
# Tensorflow 1.10
# Other combinations may break: https://github.com/tensorflow/tensorflow/issues/15604
# After completion, you should reboot the instance

# setup Python3.6 with pip and venv
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.6-dev
sudo curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6
sudo apt install python3.6-venv

# Install CUDA
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
sudo apt update
sudo apt install cuda -y
echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc1
echo 'export PATH=$PATH:$CUDA_HOME/bin' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$CUDA_HOME/lib64' >> ~/.bashrc
source ~/.bashrc

# Install cuDNN / https://developer.nvidia.com/rdp/cudnn-download
gsutil cp gs://roboy-deep-control-cudnn-drivers/cudnn-9.0-linux-x64-v7.tgz .
tar -xzvf cudnn-9.0-linux-x64-v7.tgz
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*

rm cudnn-9.0-linux-x64-v7.tgz
rm -rf cuda/

# Install Tensorflow-GPU
python3.6 -m venv env
source env/bin/activate
python3.6 -m pip install tensorflow-gpu==1.10

# Install and configure jupyter
python3.6 -m pip install jupyter
$(which jupyter) notebook --generate-config
echo "c = get_config()" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.ip = '*'" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.open_browser = False" >> $HOME/.jupyter/jupyter_notebook_config.py
echo "c.NotebookApp.port = 8888" >> $HOME/.jupyter/jupyter_notebook_config.py

# Install OpenAI baselines requirements
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev -y

sudo reboot
