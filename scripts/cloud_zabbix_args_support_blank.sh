#!/bin/bash

filepath=$(dirname "$0")

if [ $# -lt 2 ];then 
    echo "Invalid parameter! $*"
    exit 1
fi

filename=$1

if [ -f "${filepath}/${filename}.sh" ];then
    file="${filepath}/${filename}.sh"
elif [ -f "${filepath}/${filename}.py" ];then
    file="${filepath}/${filename}.py"
else
    exit 1
fi

shift

ps -aux | grep "$file $*" | grep -v "grep" >/dev/null 2>&1
if [ $? = 1 ]; then
    $file "$@"
else
    echo "The same command running!"
fi
