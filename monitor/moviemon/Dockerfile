FROM python:3.10-bullseye as checkout

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN apt-get update && \
    apt-get -q -y upgrade

RUN git clone -b moviemon https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b moviemon https://github.com/cloudpassion/modules --depth 1
RUN cd deploy && wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh

RUN ln -s  . && \
    cd moviemon && \
    ln -s ../modules my

COPY .secrets.yml moviemon/

ARG PATH=deploy/monitor/moviemon

ENTRYPOINT "deploy/run.sh"
CMD ["${PATH}"]



