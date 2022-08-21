#!/bin/bash -ex

if [ "$#" != "1" ]; then
    echo "specify backup host"
    exit 1
fi

if [ -e jobs ]; then
    echo "clearing existing jobs"
    rm -rf jobs/*
fi

./get-volumes.sh
python3 gen.py ${1} /home/anubis/backups/volumes/$(date +%Y%m%d)/
./run_jobs.py
