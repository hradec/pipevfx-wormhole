#!/bin/bash

CD=$(readlink -f $(dirname $(readlink -f $0))/../)

extra=" -ti "
if [ "$DAEMON" != "" ] ; then
	extra=" --restart always --detach "
fi

volumes=""
for each in $(ls -1 /*/.root) ; do
	volumes="$volumes -v $each:$each "
done

docker build $CD/docker/ -t hradec/streamlit
docker rm -f streamlit
docker run --name streamlit $extra \
	--net host \
	-e HOME=$HOME \
	-e USER=$USER \
	$volumes \
	-v /etc/passwd:/etc/passwd \
	-v /home/$USER:$(readlink -f /home/$USER) \
	-v $CD:$CD \
	-v $CD:/data \
hradec/streamlit "$@"
