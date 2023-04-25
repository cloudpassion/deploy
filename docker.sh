#!/bin/bash
#
echo get variables from Dockerfile ...

for variable_value in $(cat /proc/1/environ | sed 's/\x00/\n/g'); do
    export $variable_value
done

# temp
export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

echo show variables from Dockerfile ...

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
