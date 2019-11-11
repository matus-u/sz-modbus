#!/bin/bash

MAC=$(ifconfig eth0 | grep ether | tr -s ' ' | cut -f 3 -d ' ' | tr -s ':' '_')

. generate-from-uic.sh

generate-from-uic

if [ -e /dev/ttyUSB0 ]; then 
	export DEVICES_ATTACHED=TRUE
fi

python3 Main.py "[$MAC]"
