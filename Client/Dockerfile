FROM ubuntu:16.04
      
MAINTAINER Shermin Shojaei

RUN apt-get update
RUN apt-get upgrade -y

# add more stuff here
#open ssh server

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd


ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 10023

#mcperf
ADD https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/twemperf/mcperf-0.1.1.tar.gz /tmp/  
RUN apt-get update  -y &&\
  apt-get install build-essential -y &&\
tar -xvzf /tmp/mcperf-0.1.1.tar.gz &&\
cd mcperf-0.1.1 &&\
./configure &&\
make &&\
make install

#R
RUN apt-get install -y r-base-core
COPY graphs.R /

ADD dude /
RUN python setup.py install
COPY Dudefile /
CMD ["/usr/sbin/sshd", "-D"]
