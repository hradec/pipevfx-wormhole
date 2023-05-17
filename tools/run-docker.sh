#!/bin/bash

CD=$(readlink -f $(dirname $(readlink -f $0))/../)

extra=" -ti "
if [ "$DAEMON" != "" ] ; then
	extra=" --restart always --detach "
fi

volumes=""
for each in $(ls -1 /*/.root) ; do
	each=$(dirname $each)
	volumes="$volumes -v $each:$each "
done
for each in $(ls -1 $CD/scripts/*) ; do
	abs=$(dirname $(readlink -f $each))
	abs=$(df -h $abs | grep -v Size | awk '{print $(NF)}')
	if [ "$(echo $volumes | grep $abs)" == "" ] ; then
		volumes="$volumes -v $abs:$abs "
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
	-v /home/$USER:$(readlink -f /home/$USER) \
	-v $CD:$CD \
	-v $CD:/data \
hradec/streamlit "$@"
