#!/bin/bash

sudo apt update -y
sudo apt upgrade -y

#setup python
sudo apt install python3-pip -y
sudo apt python-is-python3 -y
sudo apt install build-essential -y
sudo apt install python3-venv -y

#setup environment
python -m venv .venv
source .venv/bin/activate

#update pip and setup installs
python -m pip install --upgrade pip setuptools wheel

#install
pip install .

pip install build-essential -y



# Install CMake, gcc, g++ and other build essentials
sudo apt install build-essential -y

# Install ffmpeg
sudo apt install ffmpeg -y

# Install zlib
sudo apt-get install zlib1g -y

# Install NVIDIA utilities
sudo apt install nvidia-utils-535 -y

# Create a symbolic link for CUDA
sudo ln -sf /sbin/ldconfig.real /usr/lib/wsl/lib/libcuda.so.1

#delete the 7fa2af80 key
sudo apt-key del 7fa2af80

# Download and Install CUDA
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-debian11-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo dpkg -i cuda-repo-debian11-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-debian11-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo add-apt-repository contrib
sudo apt-get update
sudo apt-get -y install cuda

# Update repositories
sudo apt update -y


#Install fairseq2
sudo apt install libsndfile1 -y

git clone "https://github.com/facebookresearch/fairseq2.git"
cd fairseq2

pip install fairseq2 --extra-index-url https://fair.pkg.atmeta.com/fairseq2/whl/pt2.0.1/cu118

git clone --recurse-submodules https://github.com/facebookresearch/fairseq2.git -y

cd fairseq2

git submodule update --init --recursive

sudo apt install libsndfile-dev -y

echo"" > requirements-build.txt

pip install -r fairseq2n/python/requirements-build.txt 

cd fairseq2n

cmake -GNinja -DFAIRSEQ2N_USE_CUDA=ON -B build

cmake --build build
git submodule update --init --recursive
