#!/bin/bash

echo export some variables

for variable_value in $(cat /proc/1/environ | sed 's/\x00/\n/g'); do
    export $variable_value
done

# temp
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

echo show get variables from Dockerfile ...

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
    rsync -avL -e "ssh -o BatchMode=yes -p ${port}" "${url}":${tag}/ .
    if [ $? -eq 0 ]; then
       touch ~/.deployed
    fi
fi

echo updating packages ...
pip install -U -r requirements.txt

echo PWD:$PWD
echo "ls:$(ls)"

echo executing $script in $(python --version) ...

if [ -f $test_script ]; then
    python $test_script
    if [ $? -ne 0 ]; then
        echo not pass tests
    fi
fi

if [[ "$test_script" != "$script" ]]; then
    python $script
fi
