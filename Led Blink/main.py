from machine import Pin
from time import sleep

led = Pin(15,Pin.OUT) 

while True: # a infinate loop
	led.value(1) # turns on the led    
	sleep(0.5) # pauses the code for 0.5 seconds 
	led.value(0) # turns off the led 
	sleep(0.5)
