#!/bin/bash

CD=$(dirname $(readlink -f $BASH_SOURCE))
cd $CD

if [ "$1" == "-d" ] ; then
	export DAEMON=1
fi
if [ "$1" == "-l" ] ; then
	docker logs -f streamlit
	exit 0
fi
if [ "$1" == "-s" ] ; then
	docker exec -ti streamlit /bin/bash
	exit 0
fi
if [ "$1" == "-h" ] ; then
	echo -e "
	$(basename $0)

 		-d	run in daemon mode
		-l	display daemon log
		-s	run a shell in the container running the daemon (for debugging)
	"
	exit 0
fi
./tools/run-docker.sh python3 -m streamlit run --theme.base dark ./python/scripts.py
