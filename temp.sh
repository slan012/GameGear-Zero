#!/bin/bash

# display CPU temp

cpu_temp=$(cat /sys/class/thermal/thermal_zone0/temp)
let 'cpu_temp0 = cpu_temp/1000'
echo "CPU temp : $cpu_temp0"


