FROM ubuntu:16.04
MAINTAINER Shermin Shojaei

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added

RUN groupadd -r memcache && useradd -r -g memcache memcache
RUN apt-get update && apt-get install -y --no-install-recommends \
		libevent-2.0-5 \
	&& rm -rf /var/lib/apt/lists/*

ENV MEMCACHED_VERSION 1.4.33
ENV MEMCACHED_SHA1 e343530c55946ccbdd78c488355b02eaf90b3b46

RUN buildDeps=' \
		gcc \
		libc6-dev \
		libevent-dev \
		make \
		perl \
		wget \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& wget -O memcached.tar.gz "http://memcached.org/files/memcached-$MEMCACHED_VERSION.tar.gz" \
	&& echo "$MEMCACHED_SHA1  memcached.tar.gz" | sha1sum -c - \
	&& mkdir -p /usr/src/memcached \
	&& tar -xzf memcached.tar.gz -C /usr/src/memcached --strip-components=1 \
	&& rm memcached.tar.gz \
	&& cd /usr/src/memcached \
	&& ./configure \
	&& make -j$(nproc) \
	&& make install \
	&& cd / && rm -rf /usr/src/memcached \
	&& apt-get purge -y --auto-remove $buildDeps

COPY docker-entrypoint.sh /
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat


#start of SSH

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 10022
RUN chmod 755 /docker-entrypoint.sh
CMD ["/usr/sbin/sshd", "-D"]
