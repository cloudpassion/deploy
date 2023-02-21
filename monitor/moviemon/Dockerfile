FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN apt-get update && \
    apt-get -q -y upgrade

ARG branch=moviemon
ARG path="deploy/monitor/moviemon"

ENV branch="${branch}"
ENV path="${path}"

ENV TEST="work test"

RUN git clone -b ${branch} https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b ${branch} https://github.com/cloudpassion/modules --depth 1
RUN cd deploy && wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh -O _run.sh

RUN ln -s ${path} . && \
    cd /moviemon && \
    ln -s ../modules my

RUN echo "script=${branch}" >> /deploy/run.sh
RUN echo "path=${path}" >> /deploy/run.sh
RUN echo "$DATA" >> /deploy/run.sh
RUN cat /deploy/_run.sh >> deploy/run.sh

RUN cat deploy/run.sh

#RUN chmod +x /deploy/run.sh

COPY .secrets.yml /moviemon/

ENTRYPOINT "/deploy/run.sh"


