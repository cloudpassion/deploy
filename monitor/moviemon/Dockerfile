FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

# update packages and download sources
RUN apt-get update && \
    apt-get -q -y upgrade

ARG branch="moviemon"
ARG path="deploy/monitor/${branch}"

# grab sources for specific branch
# and download startup script
RUN git clone -b "${branch}" https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b "${branch}" https://github.com/cloudpassion/modules --depth 1
RUN cd "${path}" && pip install -r requirements.txt

ARG RUN=0
RUN RUN=${RUN} wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh -O deploy/run.sh
RUN chmod +x /deploy/run.sh

# set script name and location for runtime

ENV branch="${branch}"
ENV script="test.py"

RUN ln -s "${path}" "${branch}" && \
    cd /"${branch}" && \
    ln -s /modules my

# copy settings
COPY .secrets.yml /"${branch}"/
#COPY settings.yml /"${branch}"/

ENTRYPOINT "/deploy/run.sh"

