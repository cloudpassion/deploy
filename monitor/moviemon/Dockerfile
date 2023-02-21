FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN apt-get update && \
    apt-get -q -y upgrade

ENV branch="moviemon"
ENV path="deploy/monitor/moviemon"

RUN git clone -b ${branch} https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b ${branch} https://github.com/cloudpassion/modules --depth 1
RUN cd deploy && wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh

RUN ln -s ${path} . && \
    cd moviemon && \
    ln -s ../modules my

COPY .secrets.yml moviemon/


ENTRYPOINT "deploy/run.sh"
CMD ["${PATH}"]



