#!/usr/bin/env python

# A simple Python application for controlling a relay board from a Raspberry Pi
# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

import sys
import RPi.GPIO as GPIO


# change this value based on which GPIO port the relay is connected to
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



# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
# relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

# relay.on()
# def set_relay(status):
#     if status:
#         print("Setting relay: ON")
#         relay.on()
#     else:
#         print("Setting relay: OFF")
#         relay.off()


# def toggle_relay():
#     print("toggling relay")
#     relay.toggle()


# def main_loop():
#     # start by turning the relay off
#     set_relay(False)
#     while 1:
#         # then toggle the relay every second until the app closes
#         toggle_relay()
#         # wait a second 
#         time.sleep(1)


# if __name__ == "__main__":
#     try:
#         main_loop()
#     except KeyboardInterrupt:
#         # turn the relay off
#         set_relay(False)
#         print("\nExiting application\n")
#         # exit the application
#         sys.exit(0)