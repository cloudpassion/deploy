FROM python:3.10-bullseye
LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN apt-get update && \
    apt-get -q -y upgrade

RUN git clone -b moviemon https://github.com/cloudpassion/deploy moviemon
RUN git clone -b moviemon https://github.com/cloudpassion/modules moviemon/my
RUN pip install -r moviemon/requirments.txt

COPY .secrets.yml moviemon/

CMD ["python3", "moviemon/test.py"]



