#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO


# The PIN Number - Not the GPIO number. See central numbers on https://www.electronicwings.com/raspberry-pi/raspberry-pi-gpio-access
RELAY_PIN = 8

if(len(sys.argv) < 2):
	print("Supply a parameter ON or OFF")
	exit(1)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT)

if(sys.argv[1] == "ON"):
	print("Pin "+str(RELAY_PIN)+" ON")
	GPIO.output(RELAY_PIN, 0)
	exit(0)

if(sys.argv[1] == "OFF"):
	print("Pin "+str(RELAY_PIN)+" OFF")
	GPIO.output(RELAY_PIN, 1)
	exit(0)

print("Supply a parameter ON or OFF")
exit(2)
