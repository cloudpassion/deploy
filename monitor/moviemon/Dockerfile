FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

# update packages and download sources
RUN apt-get update && \
    apt-get -q -y upgrade

ARG branch="moviemon"

# grab sources for specific branch
# and download startup script
RUN git clone -b "${branch}" https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b "${branch}" https://github.com/cloudpassion/modules --depth 1

ARG RUN=0
RUN wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh -O deploy/run.sh
RUN chmod +x /deploy/run.sh

# set script name and location for runtime

ENV branch="${branch}"
ENV path="deploy/monitor/${branch}"

ENV script="test.py"

# copy settings
COPY .secrets.yml /"${branch}"/
#COPY settings.yml /"${branch}"/

ENTRYPOINT "/deploy/run.sh"

