#!/bin/bash
xhost local:root
DEVICE=/dev/ttyUSB0

if [ ! -e /dev/ttyUSB0 ];
then 
    DEVICE=/dev/zero
fi

docker run -it --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd)/modbus-app:/src/app \
    -e DISPLAY=$DISPLAY \
    --device=$DEVICE \
    modbus-app
