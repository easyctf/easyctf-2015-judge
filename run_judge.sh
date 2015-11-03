#!/usr/bin/env bash

BASE_DIR=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
cd ${BASE_DIR}

git reset --hard
git pull

wait_for_exit(){
    for pid in "$@"; do
        while kill -0 "$pid"; do
            sleep 0.5
        done
    done
}

if [ -e judge.pid ]
then
    prevpid=$(cat judge.pid)
    if [ -n ${prevpid} ] && kill -0 ${prevpid} 2>/dev/null
    then
        kill ${prevpid}
        wait_for_exit ${prevpid}
    fi
fi
if [ -e db_setup.sh ]
then
    . ./db_setup.sh
else
    echo "db_setup.sh missing"
fi
BASE_DIR=${BASE_DIR} nohup python3 main.py &
echo -n $! > judge.pid