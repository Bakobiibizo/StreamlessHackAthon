pip install build-essential -y

git clone --recurse-submodules https://github.com/facebookresearch/fairseq2.git -y

cd fairseq2

git submodule update --init --recursive

sudo apt install libsndfile-dev -y

pip install -r fairseq2n/python/requirements-build.txt 

cd fairseq2n

cmake clean

cmake -GNinja -B build

cmake --build build