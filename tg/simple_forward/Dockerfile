FROM python:3.10-bullseye

# this Dockerfile for python script
# run and forget variant without reload
# all excepts grabbing in script
# exit script stopping docker container

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -N ""
RUN cat ~/.ssh/id_rsa.pub

# update packages and download sources
RUN apt-get update && \
    apt-get -q -y upgrade
RUN apt-get -q -y install wget rsync
RUN apt-get -q -y install cron

# change
ARG entry_script="python.sh"
ARG branch="tg_forward_sh"

ARG path="deploy/monitor/${branch}"

# grab sources for specific branch
# and download startup script
RUN git clone -b "${branch}" https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b "${branch}" https://github.com/cloudpassion/modules --depth 1
RUN cd "${path}" && pip install -r requirements.txt

RUN wget https://raw.githubusercontent.com/cloudpassion/deploy/main/"${entry_script}"
RUN chmod +x /"${entry_script}"

# set script name and location for runtime

ENV branch="${branch}"

RUN ln -s "${path}" "${branch}" && \
    cd /"${branch}" && \
    ln -s /modules my && \
    ln -s /modules/* .

# prod
ENV test_script="test.py"
# change
ENV script="tr_forward_simple.py"

# change
ENV tag tr_forward_sh

ENV rsync y
ENV url pysync@192.168.55.181
ENV port 10321

# update startup script and run it on boot
CMD wget -N https://raw.githubusercontent.com/cloudpassion/deploy/main/"${entry_script}" ; 
    chmod +x "${entry_script}" ; 
    ./"${entry_script}"


