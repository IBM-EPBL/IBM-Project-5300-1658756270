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

#Python program for traffic light on Raspberry Pi

from gpiozero import Button, TrafficLights, Buzzer    
from time import sleep    
    
buzzer = Buzzer(15)    
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
    
while True:    
           button.wait_for_press()   
           buzzer.on()   
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1)    
           lights.off()   
           buzzer.off()
