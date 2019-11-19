#!/bin/bash

if [ "$1" == "" ];
then
	echo "Provide ip address of target device!"
	exit 1
fi

#TODO FIRST INSTALL TO UNKNOWN BOARD FROM USB WITH OTHER SCRIPT

sudo rm -rf modbus-app/generated/*
sudo rm -rf modbus-app/configs/*
sudo find modbus-app/ -name "__py*" | sudo xargs rm -rf
ssh root@$1 "rm -rf /media/usbstick/modbus-app/" 
scp -r modbus-app root@$1:/media/usbstick/
