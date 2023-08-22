#!/bin/bash

CD=$(dirname $(readlink -f $BASH_SOURCE))
if [ "$DOCKER" != "" ] ; then
	CD=/venv
	mkdir -p $CD
fi
echo $CD
cd $CD

export CUDA_HOME=/opt/cuda/

/usr/bin/python3 -m ensurepip
/usr/bin/python3 -m pip install virtualenv
pv=$(/usr/bin/python3 -c 'import sys;print(sys.version)' | head -1 | awk -F'.' '{print $1"."$2}')
/usr/bin/python3 -m virtualenv -p /usr/bin/python3  $CD/env.$pv

. env.$pv/bin/activate
python3 -m ensurepip
python3 -m pip install -U pip


#git clone http://github.com/alembic/alembic $CD/alembic-git
#cd $CD/alembic-git
#rm -rf build
#mkdir build
#cd build
#cmake ../  -DUSE_PYALEMBIC=1
#make -j 8

python3 -m pip install -U streamlit-autorefresh
python3 -m pip install -U streamlit
python3 -m pip install st_btn_select
python3 -m pip install psutil
python3 -m pip install matplot
#./env.$pv/bin/python3 -m pip install -U setuptools
# ./env.$pv/bin/python3 -m pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
#./env.$pv/bin/python3 -m pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
#./env.$pv/bin/python3 -m pip install opencv-python matplotlib
#./env.$pv/bin/python3 -m pip install spyder
#./env.$pv/bin/python3 -m pip install -U 'git+https://github.com/IDEA-Research/GroundingDINO.git'
#./env.$pv/bin/python3 -m pip install -U 'git+https://github.com/facebookresearch/segment-anything.git'
#./env.$pv/bin/python3 -m pip install -U git+https://github.com/luca-medeiros/lang-segment-anything.git

if [ 1 -eq 0 ] ; then

#rm -rf ./env.$pv/lib/python3.9/site-packages/open3d*
./env.$pv/bin/python3 -m pip install $CD/src/open3d_cpu-0.17.0+a5be78cfe-cp39-cp39-manylinux_2_32_x86_64.whl
./env.$pv/bin/python3 -m pip install cython
./env.$pv/bin/python3 -m pip install usd-core
./env.$pv/bin/python3 -m pip install requests
./env.$pv/bin/python3 -m pip install flask
./env.$pv/bin/python3 -m pip install pyheif
./env.$pv/bin/python3 -m pip install pyexif
./env.$pv/bin/python3 -m pip install piexif
./env.$pv/bin/python3 -m pip install "exifread<3"
./env.$pv/bin/python3 -m pip install PySide2
./env.$pv/bin/python3 -m pip install numpy
./env.$pv/bin/python3 -m pip install opencv-python


#./env.$pv/bin/python3 -m pip install torch
#./env.$pv/bin/python3 -m pip install torchvision
#./env.$pv/bin/python3 -m pip install pyyaml
#./env.$pv/bin/python3 -m pip install matplotlib
#./env.$pv/bin/python3 -m pip install scipy
#./env.$pv/bin/python3 -m pip install scikit-fmm
./env.$pv/bin/python3 -m pip install scikit-image
fi
