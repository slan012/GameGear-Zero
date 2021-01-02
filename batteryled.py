#!/usr/bin/python

##################################################################
## This script makes red power LED blinking when Li-ion battery ##
## voltage is lower than BATT_VOLTAGE_ALERT                     ##
##################################################################

# import libs

import RPi.GPIO as GPIO
from time import sleep
from ads1015 import ADS1015

# init consts
CHANNEL = 'in1/gnd'
BATT_VOLTAGE_ALERT = 3.290
TIME = 0.3 # LED blinking interval
PIN = 16 # GPIO output for LED

# setup ads1015
ads1015 = ADS1015()
ads1015.set_mode('single')
ads1015.set_programmable_gain(4.096)
ads1015.set_sample_rate(1600)

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.HIGH)

def led_blink(time):
	GPIO.output(PIN, GPIO.LOW)
	sleep(time)
	GPIO.output(PIN, GPIO.HIGH)
	sleep(time)

try:
    while True:
    	batt_voltage = ads1015.get_voltage(CHANNEL)
    	if batt_voltage < BATT_VOLTAGE_ALERT:
    		# sleep 5 sec to confirm voltage
    		sleep(2)
    		batt_voltage = ads1015.get_voltage(CHANNEL)
    		if batt_voltage < BATT_VOLTAGE_ALERT:
                    while True:
                        led_blink(TIME);
                        batt_voltage = ads1015.get_voltage(CHANNEL)
                        if batt_voltage > BATT_VOLTAGE_ALERT: 
                            GPIO.output(PIN, GPIO.HIGH)
                            break

        sleep(10)
except KeyboardInterrupt:
    pass