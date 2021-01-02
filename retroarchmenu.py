#!/usr/bin/python

import RPi.GPIO as GPIO  
from time import sleep
import socket  
# addressing information of target  
IPADDR = "127.0.0.1"  
PORTNUM = 55355  
# enter the data content of the UDP packet  
COMMAND = "MENU_TOGGLE"  
# initialize a socket, think of it as a cable  
# SOCK_DGRAM specifies that this is UDP  
try:  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
except socket.error:  
    print 'Failed to create socket'  
    sys.exit()  
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # START button
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) # A button 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # B button

def openMenu():  
    s.sendto(COMMAND, (IPADDR, PORTNUM))  

try:
	while True:
		GPIO.wait_for_edge(10, GPIO.FALLING)
		if GPIO.input(25) == GPIO.LOW and GPIO.input(24) == GPIO.LOW:
			openMenu()
		sleep(0.2)

except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()

