FROM debian:10

ENV DOCKER=1

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN dpkg --add-architecture i386

RUN apt update
RUN apt install -y python3 python3-pip

COPY install_virtualenv.sh /root/install_virtualenv.sh

RUN /root/install_virtualenv.sh
RUN chmod a+rwx -R /root/

COPY init.sh /init.sh
RUN chmod a+rx -R /init.sh

RUN apt install -y curl wget
RUN apt install -y sudo htop net-tools
RUN apt install -y python2
RUN apt install -y procps
RUN apt install -y binutils

# chrome need this to run and return the version with --version
RUN apt install libc6-i386
RUN apt install -y \
        libglib2.0-0 \
        libnss3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 libdrm2 \
        libxcomposite1 \
        libxkbcommon0 \
        libpango-1.0-0 \
        libcairo2 \
        libasound2 \
        libxdamage1 \
        libxrandr2 \
        libgbm1

RUN apt install -y sudo
RUN apt install -y rsync
RUN apt install -y libxxf86vm1

# we need nodejs for scrapping using puppeteer
#RUN apt install -y nodejs npm

# blender 3.5 needs this now
RUN apt install -y libsm6
RUN apt install -y unzip
RUN apt install -y cron jq

ENTRYPOINT ["/init.sh"]
