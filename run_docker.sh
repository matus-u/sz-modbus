#!/bin/bash
xhost local:root
docker run -it --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v $(pwd)/modbus-app:/src/app \
    -v /dev:/dev \
    -e DISPLAY=$DISPLAY \
    modbus-app
