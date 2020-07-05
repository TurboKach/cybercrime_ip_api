# Version: 0.0.1
FROM ubuntu:18.04
MAINTAINER Maxim Karpov <incognito@turbokach.me>
WORKDIR /home/$USER/
RUN apt-get update
RUN apt-get install -y apt-utils
COPY . .
RUN  ./firehol-install.sh
RUN apt-get install -y python3.8
RUN apt-get install -y python-pip
RUN pip install https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir ~/ipsets
#  When run as root, update-ipsets keeps its files in /etc/firehol/ipsets. Otherwise they will be in ~/ipsets.
RUN update-ipsets --enable-all
EXPOSE 8000
CMD [ "python", "manage.py", "runserver"]
