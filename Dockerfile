# Version: 0.0.1
FROM ubuntu:18.04
MAINTAINER Maxim Karpov <incognito@turbokach.me>
WORKDIR /home/$USER/
RUN apt-get update
COPY . .
RUN  ./firehol-install.sh
RUN apt-get install python
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir ~/ipsets
#  When run as root, update-ipsets keeps its files in /etc/firehol/ipsets. Otherwise they will be in ~/ipsets.
RUN update-ipsets --enable-all
EXPOSE 8000
CMD [ "python", "manage.py", "runserver"]
