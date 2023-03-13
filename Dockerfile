FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update

# Python support
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pytest colorama requests

# Java/Maven support
#RUN apt-get install -y openjdk-8-jdk
#RUN apt-get install -y maven
RUN apt-get install -y nodejs npm
RUN npm i -g yarn

# stress-ng
RUN apt-get install -y stress-ng

COPY shaker /__shaker
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
