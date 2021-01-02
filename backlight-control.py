#!/usr/bin/python

##################################################################################
### Read potentiometer signal so to change MPI3508 screen backlight     ##########
### GPIO signal is sent to the backlight push button of MPI3508   ##########
##################################################################################
import RPi.GPIO as GPIO
from ads1015 import ADS1015
from time import sleep

# ads1015 setup
channel = 'in0/gnd'
sensibility = 0.2 # Modify the number of sent signals to backlight switch
ads1015 = ADS1015()
ads1015.set_mode('single')
ads1015.set_programmable_gain(4.096)
ads1015.set_sample_rate(1600)

# GPIO setup
OUTPUT_CHANNEL = 5
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_CHANNEL, GPIO.OUT, initial=GPIO.HIGH)

while True:
    value1 = ads1015.get_voltage(channel)
    while True:
        value2 = ads1015.get_voltage(channel)
        value_delta = value1 - value2
        if value_delta > sensibility or value_delta < -sensibility:
            # sleep(0.1) and read value again to ensure that is not erratic variation)
            sleep(0.1)
            value2 = ads1015.get_voltage(channel)
            value_delta = value1 - value2
            if value_delta > sensibility or value_delta < -sensibility:
                GPIO.output(OUTPUT_CHANNEL, GPIO.LOW)
                sleep(0.05)
                GPIO.output(OUTPUT_CHANNEL, GPIO.HIGH)
                break
        sleep(0.3)
