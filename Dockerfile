FROM python:3.10

# Add ssh private key into container
ARG ssh_prv_key
ARG ssh_pub_key

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# set Workdir
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN git config --global user.email "giraud.nicolas@me.com" \ 
    && git config --global user.name "Lecogoni"


CMD tail -f /dev/null
# RUN git init --initial-branch=main
# RUN git remote add origin git@gitlab.com:eshop-padel-javascript/node-api.git


