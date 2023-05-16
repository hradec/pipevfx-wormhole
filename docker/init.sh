#!/bin/bash

CD=$(dirname $(readlink -f $BASH_SOURCE))
if [ "$DOCKER" != "" ] ; then
        CD=/venv
        mkdir -p $CD
fi
echo $CD


	pv=$(/usr/bin/python3 -c 'import sys;print(sys.version)' | head -1 | awk -F'.' '{print $1"."$2}')
	source $CD/env.$pv/bin/activate


	#export LD_LIBRARY_PATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/cortex/10.3.4.0/lib/boost.1.66.0/
	#export LD_LIBRARY_PATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/ilmbase/2.4.1/boost.1.66.0/lib/
	#export	LD_LIBRARY_PATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/llvm/10.0.1/lib/:$LD_LIBRARY_PATH
	#export LD_LIBRARY_PATH=/usr/lib64/llvm10/lib/:$LD_LIBRARY_PATH
	#export LD_LIBRARY_PATH=$HOME/dev/xcode-13-acesso/photo-ruler/env.3.9/lib/python3.9/site-packages/open3d/:$LD_LIBRARY_PATH


	export PYTHONPATH=$CD/src/insulin_calculator/insulin_calculator_server/fvolume/:$PYTHONPATH
	export PYTHONPATH=$CD/src/insulin_calculator/insulin_calculator_server/fvolume/c_core:$PYTHONPATH
	export PYTHONPATH=$CD/src/insulin_calculator/insulin_calculator_server/fvolume/c_core:$PYTHONPATH
	#export PYTHONPATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/cortex/10.3.4.0/lib/boost.1.66.0/python3.9:$PYTHONPATH
	#export PYTHONPATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/cortex/10.3.4.0/lib64/boost.1.66.0/python3.9/site-packages/:$PYTHONPATH
	#export PYTHONPATH=/atomo/pipeline/libs/linux/x86_64/pipevfx.5.0.0/ilmbase/2.4.1/boost.1.66.0/lib/python3.9/site-packages/:$PYTHONPATH
	#$CD/env.$pv/bin/python3 "$@"

export HOME
export USER
cd /data
echo "$@" | runuser $USER -c /bin/bash
