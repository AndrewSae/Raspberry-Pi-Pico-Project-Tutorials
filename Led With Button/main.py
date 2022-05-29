from machine import Pin

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
    	led.value(1)
    else:
        led.value(0)

