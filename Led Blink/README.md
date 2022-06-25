## Led Blink project

In this first project you will learn how to interface a led with the Pi Pico the proper way.

## Required parts:
- Raspberry Pi Pico
- Breadboard 
- A led 
- 220Ω resistor
- 2x male to male hookup wires 

## Setup the circuit:
- Step 1:
  - First place the Pi Pico on the breadboard and then connect pin 38(GND) to the ground bus of the breadboard, it should look something like this:          ![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20Blink/Circuit/step1.png?raw=true)

- Step 2:
  - Next place the ground leg(the shorter leg) of the led into the ground bus that is connected to the ground pin on the pico and the positive leg(the longer leg) into a row of a breadboard that is not on the power bus, it should look something like this
![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20Blink/Circuit/step2.png?raw=true)


- Step 3:
  - Now connect the one leg of the 220Ω resistor into the same row that the leds positive leg is in then connect the other leg of the resistor into a completely different row of the breadboard, it should look something like this:
![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20Blink/Circuit/step3.png?raw=true)

- Step 4:
  - Lastly take another hookup wire and connect it to the leg of the resistor that is not in the same row as the positive leg of the led and take the other end of the wire and connect it to pin 20 (GPIO 15)
![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20Blink/Circuit/step4.png?raw=true)


## Code setup
Firstly we need to import the required modules 

We will be using the ```Pin``` module to interface with the led and the ```sleep``` module to make the code pause for a set amount of time 

```python
from machine import Pin
from time import sleep
```

Next we need to make a variable that will allow us to control the led 

To do this we will use the ```Pin()``` function we will need to pass in the gpio pin number in our case it is ```15``` and then we need to pass in ```Pin.OUT``` so we can use the specified gpio pin as an output

``` python 
led = Pin(15,Pin.OUT) 
```

To turn on and off the led we will be using the ```toggle()``` function 

The ```toggle()``` function will always do the opposite of what the pins status is if the pin is sending power to the led and you call the ```toggle()``` function the pin will stop sending power to the led

Now to make it blink we will need a ```while True:```  then we need to call the ```toggle()``` function to turn the led on next we will use the ```sleep()``` function to keep the led on for a certain amount of time then on the next pass of the loop the ```toggle()``` function will turn off the led and so on

```python 
while True: 
	led.toggle()    
	sleep(0.5) 
```


Full code
```python 

from machine import Pin
from time import sleep

led = Pin(15,Pin.OUT) 

while True: 
	led.toggle()    
	sleep(0.5) 
```

(Note that the code can also be found in the [main.py](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/Led%20Blink/main.py) file)

## Run the code:

Save the code to the pico and press the run button if you made all the connections correctly you will see the led flashing 

## Challenge:
Add another led to the circuit and make it so that the leds alternate what one is off

