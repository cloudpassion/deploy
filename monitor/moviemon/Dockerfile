FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN apt-get update && \
    apt-get -q -y upgrade

# set script name and location for build and run
ARG branch=moviemon
ARG path="deploy/monitor/moviemon"

ENV branch="${branch}"
ENV path="${path}"

RUN git clone -b ${branch} https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b ${branch} https://github.com/cloudpassion/modules --depth 1
RUN wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh -O deploy/run.sh

# create symlink in root for script dir
RUN ln -s ${path} . && \
    cd /"${branch}" && \
    ln -s /modules my

RUN chmod +x /deploy/run.sh

# copy settings
COPY .secrets.yml /moviemon/

#
ENTRYPOINT "/deploy/run.sh"


