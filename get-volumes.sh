#!/bin/sh

kubectl get pvc -n anubis | awk '/ide-volume/ {print "\""$1"\""}' | jq -s | tee volumes.json
