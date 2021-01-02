#!/usr/bin/python
#Import libs
import RPi.GPIO as GPIO
import os
import time
#Set Environment
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # START button
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # A button
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DOWN button
#Code
flag = True

try:
	while flag:
		GPIO.wait_for_edge(10, GPIO.FALLING)
		if GPIO.input(25) == GPIO.LOW and GPIO.input(17) == GPIO.LOW:
			pressedat = time.clock()
			while GPIO.input(10) == GPIO.LOW and GPIO.input(25) == GPIO.LOW and GPIO.input(17) == GPIO.LOW:
				releasedat = time.clock()
				if (releasedat - pressedat) >= 1:
					flag = False
					os.system("killall -9 retroarch mupen64plus fba2x scummvm &> /dev/null")
					os.system("shutdown -h now")
					break
		else:
			pressedat = time.clock()
			while GPIO.input(10) == GPIO.LOW:
				releasedat = time.clock()
				if (releasedat - pressedat) >= 1:
					os.system("killall -9 retroarch mupen64plus fba2x scummvm &> /dev/null")
        #Reset Control Vars
		releasedat = pressedat = 0
	time.sleep(0.1)
#Cleaning Gpio ports on Error or Exit
finally:
	GPIO.cleanup()
