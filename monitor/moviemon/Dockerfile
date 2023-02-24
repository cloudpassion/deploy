FROM python:3.10-bullseye

LABEL org.opencontainers.image.authors="dock@cldvp.xyz"

RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -N ""
RUN cat ~/.ssh/id_rsa.pub

# update packages and download sources
RUN apt-get update && \
    apt-get -q -y upgrade && \
    apt-get -q -y install wget

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

RUN ln -s "${path}" "${branch}" && \
    cd /"${branch}" && \
    ln -s /modules my

# dev
#COPY .secrets.yml /"${branch}"/
#COPY settings.yml /"${branch}"/

# prod
ENV test_script="test.py"
ENV script="kn5.py"

ENV rsync n
ENV tag kn5
ENV url pysync@192.168.50.135
ENV port 10321

#ENTRYPOINT "/deploy/run.sh"

CMD wget https://raw.githubusercontent.com/cloudpassion/deploy/main/run.sh -O deploy/run.sh ; chmod +x deploy.run.sh ; ./deploy/run.sh

