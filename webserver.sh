#!/bin/bash

CD=$(dirname $(readlink -f $BASH_SOURCE))
cd $CD

if [ "$1" == "-d" ] ; then
	export DAEMON=1
fi
if [ "$1" == "-h" ] ; then
	echo -e "\n$(basename $0)\n\n\t -d = run in daemon mode\n\n"
	exit 0
fi
./tools/run-docker.sh python3 -m streamlit run --theme.base dark ./python/init.py
