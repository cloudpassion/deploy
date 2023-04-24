#!/bin/bash

echo variables from Dockerfile ...
echo url:$url
echo port:$port
echo tag:$tag

echo commands_to_run:"$1"

echo sync files
if [[ "${rsync}" == "y" && ! -f ~/.deployed ]]; then
    # tag, url, port
    rsync -avL -e "ssh -o BatchMode=yes -p ${port}" "${url}":${tag}/ .
    if [ $? -eq 0 ]; then
        touch ~/.deployed
    fi
fi

IFS=';' read -ra commands <<< "$1"
for command in "${commands[@]}"; do
    echo "executing > $command"
    eval "$command"
done
