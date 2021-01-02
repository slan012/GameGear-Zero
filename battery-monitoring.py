#!/usr/bin/python

####################################################################################
########## Monitoring the Lithium 18650 battery voltage with ADS1015  ##############
########## when voltage is lower than 3.2V -> powering off Recalbox  ###############
####################################################################################

from ads1015 import ADS1015
import time
import os

def battery_shutdown():
	flag=True
	pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
	os.system("killall -9 retroarch mupen64plus fba2x scummvm &> /dev/null")
	os.system("/etc/init.d/S31emulationstation stopbattery")
	while flag:
		flag = False
		for pid in pids:
			try:
				print pid
				commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
				if "emulationstation" in commandpath:
					flag = True
			except IOError:
				continue
	os.system("shutdown -h now")

CHANNEL= 'in1/gnd'
BATT_VOLTAGE_ALERT = 3.200

ads1015 = ADS1015()
ads1015.set_mode('single')
ads1015.set_programmable_gain(4.096)
ads1015.set_sample_rate(1600)

try:
    while True:
    	batt_voltage = ads1015.get_voltage(CHANNEL)
    	print(batt_voltage)
    	if batt_voltage < BATT_VOLTAGE_ALERT:
    		# sleep 5 sec to confirm voltage
    		time.sleep(5)
    		batt_voltage = ads1015.get_voltage(CHANNEL)
    		if batt_voltage < BATT_VOLTAGE_ALERT:
	    		battery_shutdown()
	    		break
        time.sleep(10)
except KeyboardInterrupt:
    pass
