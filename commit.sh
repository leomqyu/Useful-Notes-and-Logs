#!/bin/bash

while true; do
    git add .
    git commit -m $(date +"%y-%m-%d-%H-%M-%S")
    git push

    echo "Auto backup on $(date +"%y-%m-%d-%H-%M-%S")"
    sleep 7d
done