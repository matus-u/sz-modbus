#!/bin/bash



# start temperature check
killall -9 start-temperature.sh
scripts/./start-temperature.sh &


#while true; do
./start-app.sh
#done

