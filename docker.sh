#!/bin/bash

echo variables from Dockerfile ...
echo url:$url
echo port:$port
echo tag:$tag

echo commands_to_run:"$1"

echo sync files
if [[ "${rsync}" == "y" && ! -f ~/.deployed ]]; then
    # tag, url, port
    rsync -avL -e "ssh -p ${port}" "${url}":${tag}/ .
fi

touch ~/.deployed

IFS=';' read -ra commands <<< "$1"
for command in "${commands[@]}"; do
    echo "executing > $command"
    eval "$command"
done
