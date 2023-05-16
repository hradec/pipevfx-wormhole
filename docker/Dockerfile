FROM debian:10

ENV DOCKER=1
RUN apt update
RUN apt install -y python3 python3-pip

COPY install_virtualenv.sh /root/install_virtualenv.sh

RUN /root/install_virtualenv.sh
RUN chmod a+rwx -R /root/

COPY init.sh /init.sh
RUN chmod a+rx -R /init.sh

RUN apt install -y curl wget 

ENTRYPOINT ["/init.sh"]
