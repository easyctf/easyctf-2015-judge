#!/usr/bin/env bash

BASE_DIR=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
OUTPUT_FILE="judge.log"
cd ${BASE_DIR}

git reset --hard
git pull

if [ -e ${OUTPUT_FILE} ]
then
    for i in {1..5}
    do
        echo >> ${OUTPUT_FILE}
    done
    echo "Restarting judge..." >> ${OUTPUT_FILE}
fi

if [ ! -f db_setup.sh ]
then
    echo "db_setup.sh missing"
fi
tmux kill-session -t ctfjudge 2>/dev/null
tmux new-session -s ctfjudge -d "cd ${BASE_DIR} && . ./db_setup.sh && BASE_DIR=${BASE_DIR} python3 main.py |& tee ${OUTPUT_FILE}"