#Python program for blinking LED on Raspberry Pi

import time
import RPi.GPIO as GPIO

led_pin = 5 #Pin definition

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

GPIO.output(led_pin,GPIO.HIGH)
time.sleep(1)
GPIO.output(led_pin,GPIO.LOW)
time.sleep(1)
GPIO.output(led_pin,GPIO.HIGH)
