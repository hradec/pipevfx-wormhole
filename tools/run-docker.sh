#!/bin/bash

CD=$(readlink -f $(dirname $(readlink -f $0))/../)

extra=" -ti "
# if DAEMON is set in the environment, run the container detached
if [ "$DAEMON" != "" ] ; then
	extra=" --restart always --detach "
fi

# look for pipevfx root folder and map it as volume in docker
volumes=""
for each in $(ls -1 /*/.root) ; do
	each=$(dirname $each)
	volumes="$volumes -v $each:$each:shared "
done

# resolve the real location of every file in the scripts and data folder, and
# map it's path as a volume in docker
for each in $(ls -1 $CD/scripts/* ; ls -1 $CD/data/*) ; do
	abs=$(dirname $(readlink -f $each))
	#abs=$(df -h $abs | grep -v Size | awk '{print $(NF)}')
	if [ "$(echo $volumes | grep $abs)" == "" ] ; then
		volumes="$volumes -v $abs:$abs:shared "
	fi
done

docker build $CD/docker/ -t hradec/streamlit
docker rm -f streamlit
docker run --name streamlit $extra \
	--shm-size=16g \
	--net host \
	-e HOME=$HOME \
	-e USER=$USER \
	$volumes \
	-v /etc/shadow:/etc/shadow \
	-v /etc/passwd:/etc/passwd \
	-v /etc/sudoers:/etc/sudoers \
	-v $(readlink -f /home/$USER):$HOME:shared \
	-v $CD:$CD:shared \
	-v $CD:/data:shared \
hradec/streamlit "$@"
