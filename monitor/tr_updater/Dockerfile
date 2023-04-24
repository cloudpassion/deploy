FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -N ""
RUN cat ~/.ssh/id_rsa.pub

# update packages and download sources
RUN apt-get update && \
    apt-get -q -y upgrade
RUN apt-get -q -y install wget rsync
RUN apt-get -q -y install cron

ARG branch="tr_updater"
ARG path="deploy/monitor/${branch}"

# grab sources for specific branch
# and download startup script
RUN git clone -b "${branch}" https://github.com/cloudpassion/deploy --depth 1
RUN git clone -b "${branch}" https://github.com/cloudpassion/modules --depth 1
RUN cd "${path}" && pip install -r requirements.txt

RUN wget https://raw.githubusercontent.com/cloudpassion/deploy/main/python.sh
RUN chmod +x /python.sh

# set script name and location for runtime

ENV branch="${branch}"

RUN ln -s "${path}" "${branch}" && \
    cd /"${branch}" && \
    ln -s /modules my && \
    ln -s /modules/* .

# dev
#COPY .secrets.yml /"${branch}"/
#COPY settings.yml /"${branch}"/

# prod
ENV test_script="test.py"
ENV script="tr_update.py"

ENV rsync y
ENV tag tr_updater
ENV url pysync@192.168.55.181
ENV port 10321

RUN crontab -l | { cat; echo PYTHONUNBUFFERED=yes; } | crontab -
RUN crontab -l | { cat; echo "*/5 * * * * ps aux | grep -in ${script}.py | grep -v grep; if [ $? -eq 0 ]; then kill -9 kill -9 $(ps aux | grep -in ${script}.py | grep -v grep | awk '{print $2}'); fi ; /python.sh > /python.log 2>&1"; } | crontab -

# update startup script and run it on boot
CMD wget -N https://raw.githubusercontent.com/cloudpassion/deploy/main/python.sh ; \
    chmod +x python.sh ; /python.sh ; \
    crontab -l ; cron -f

