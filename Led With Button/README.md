## Led with button project 

In this project you will learn how to connect, get the input from a button, you will also learn how to do something with that input


## Required parts:
- Raspberry Pi Pico
- Breadboard 
- A led 
- 220Ω resistor
- A 4 leg NC button
- 5x male to male wires

## Setup the circuit:
- Step 1:
  - First place the Pi Pico on the breadboard and then connect pin 38(GND) to the ground bus of the breadboard with one of your wires, it should look something like this:          
 ![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step1.png?raw=true)


- Step 2:
  - Now connect pin 36(3V OUT) to the power bus of the breadboard with one of your wires, it should look something like this:          
 ![Step_2](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step2.png?raw=true)

- Step 3:
  - Next place the ground leg(the shorter leg) of the led into the ground bus that is connected to the ground pin on the pico and the positive leg(the longer leg) into a row of a breadboard that is not on the power bus, it should look something like this
![Step_3](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step3.png?raw=true)

- Step 4:
  - Now connect the one leg of the 220Ω resistor into the same row that the leds positive leg is in then connect the other leg of the resistor into a completely different row of the breadboard, it should look something like this:
![Step_4](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step4.png?raw=true)

- Step 5:
  - Take another wire and connect it to the leg of the resistor that is not in the same row as the positive leg of the led and take the other end of the wire and connect it to pin 20 (GPIO 15), it should look something like this:
![Step_5](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step5.png?raw=true)

- Step 6:
  - Now take the button and place it on the breadboard so that each leg has its own row on the breadboard, it should look something like this:
  ![Step_6](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step6.png?raw=true)
  
- Step 7:
  - Take another wire and connect the power bus (3V) to one leg of th button, it should look something like this:
 ![Step_7](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step7.png?raw=true)
 
- Step 8:
  - Lastly take another wire and connect one leg of the button to pin 19 (GPIO 14), it should look something like this:
 ![Step_8](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/Circuit/step8.png?raw=true)


## Code Setup:

First off we need to import the needed module 

We will be using the ```Pin``` module to control the led and to get the input from the button

``` python 
from machine import Pin
```

Next we need to set up our led and button with the ```Pin()``` function 

For the led we need to pass in the gpio pin number ```15``` and ```Pin.OUT``` to set it up as an output 

For the button we need to pass in the gpio pin number ```14``` and ```Pin.IN``` to set it up as a input pin also we need to pass in ```Pin.PULL.DOWN``` to use the integrated pull down resistor without it the pico will detect false button presses

``` python 
led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
```
Lastly we want to make a loop that will constantly be checking the buttons status in our case we will use the ```value()``` function and if that returns true(if the button is pressed) we will want to turn on the led with the same function but passing in ```1``` and if the button is not pressed we want to keep the led off by passing in ```0```

``` python 
while True:
    if button.value():
    	led.value(1)
    else:
        led.value(0)
```
(Note that the code can also be found in the [main.py](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20With%20Button/main.py) file

## Run The Code:
Save the code to the Pi Pico and once you run it you'll find that while you are holding the button down the led is on but the second you release it the led turns off 

## Challenge:
Add another button to the circuit and make it so one button turns on the led and the other will turn off the led
