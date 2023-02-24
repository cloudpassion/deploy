#!/bin/bash

echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo pulling sources ...

cd /deploy && \
    git pull --ff-only

cd /modules && \
    git pull --ff-only

echo going to workdir ...
cd /"$branch"

echo sync files
if [[ "${rsync}" == "y" && ! -f ~/.deployed ]]; then
    # tag, url, port
    rsync -avL -e "ssh -p ${port}" "${url}":${tag}/ .
fi

touch ~/.deployed

echo updating packages ...
pip install -U -r requirements.txt

echo executing $script in $(python --version) ...

if [ -f $test_script ]; then
    python $test_script
    if [ $? -ne 0 ]; then
        echo not pass tests
    fi
fi

python $script
