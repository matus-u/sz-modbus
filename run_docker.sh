#!/bin/bash
xhost local:root
docker run -it --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd)/modbus-app:/src/app \
    -e DISPLAY=$DISPLAY \
    modbus-app
    #--device=/dev/ttyUSB0 \
