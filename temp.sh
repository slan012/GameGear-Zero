#!/bin/bash

# display CPU temp

temp=$(cat /sys/class/thermal/thermal_zone0/temp)
let 'temp0 = temp/1000'
echo "CPU temp : $temp0"


