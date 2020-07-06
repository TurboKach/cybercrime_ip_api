# Version: 0.0.1
FROM ubuntu:18.04
MAINTAINER Maxim Karpov <incognito@turbokach.me>
WORKDIR /home/$USER/
COPY . .
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install -y firehol

RUN mkdir ~/ipsets
#  When run as root, update-ipsets keeps its files in /etc/firehol/ipsets. Otherwise they will be in ~/ipsets.
RUN update-ipsets --enable-all
EXPOSE 8000
CMD [ "python", "manage.py", "runserver"]
