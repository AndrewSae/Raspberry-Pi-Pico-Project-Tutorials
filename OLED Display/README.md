## OLED Display Project:
In this project you will learn how to write text to a OLED display 

## Required parts:
- Raspberry Pi Pico 
- Breadboard 
- OLED display with soldered headers (ssd1306 OLED needed)
- 6 male to male wires 

## Setup the circuit:

- Step 1:
  - Place the Pico on the breadboard then connect the GND pin (pin 38) to the ground bus of the breadboard and the 3V out pin (pin 36) to the power bus of the breadboard, it should look something like this: 
  ![Step_1](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/OLED%20Display/Circuit/setp1.png?raw=true)
 
- Step 2:
  - Place the OLED display onto the breadboard, then connect the GND pin to the ground bus on the breadboard, next connect the VCC pin to power bus of the breadboard, it should look something like this:
    ![Step_2](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/OLED%20Display/Circuit/step2.png?raw=true)

- Step 3:
  - Now connect the SCL pin (on some displays it is SCK) on the OLED to pin 22 (SCL, GPIO 17) and lastly connect the SDA pin on the OLED to pin 21 (SDA, GPIO 16), it should look something like this:
   ![Step_3](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/OLED%20Display/Circuit/step3.png?raw=true)
   
## Code setup:

The first thing we need to to is to import the required modules we will be using the ```Pin``` module to use the pins on the pico, we also need to import the ```I2C``` module so we can use the I2C pins on the pico, and we need to import the ```SSD1306_I2C``` module so we can write text to the OLED display

(note that the ```SSD1306_I2C``` is not included in micropython so in thonny go to ```tools``` > ```manage packages``` and search for ```ssd1306``` and you will see a package named ```micropython-ssd1306``` and install it also I have added the library in this project found [here](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/OLED%20Display/lib/ssd1306.py)
``` python 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
```

Next we need to make two variables that store the width and the height of the display this case the display is ```128``` pixels in width and the height is ```64``` pixels if your display is a different size the code  will still work just change the variables to match your displays dimensions

``` python 
width = 128
height = 64
```

Now we need to use the ```I2C``` function so the code knows what pins we are using first we need to pass in what I2C bus we are using in our case it is ```0``` next we need to pass in what SCL/GPIO pin we are using ```17``` and then we need to pass in what SDA/GPIO pin we are using ```16```

``` python
i2c = I2C(0, scl = Pin(17), sda = Pin(16))
```

Then we need to use the ```SSD1306_I2C()``` function so we can use the driver to write text to the OLED we need to pass in the ```width``` and the ```height``` of the display then we also need to pass in the ```i2c``` variable that we made above

``` python 
oled = SSD1306_I2C(width, height, i2c)
```

Before we can write text to the display we need to clear it by using the ```fill()``` function and by passing in ```0```
``` python 
oled.fill(0)
```

In This example we will write ```Hello World!``` to the display to do this we use the ```text()``` function  first we need to pass in the string to be shown, the ```x``` position and the ```y``` position of the text 

``` python 
oled.text("Hello World!", 10,0)
```
And to show the text we use the ```show()``` function 

``` python 
oled.show()
```

(Note that the code can also be found in the [main.py](https://github.com/AndrewSae/Raspberry-Pi-Pico-Project-Tutorials/blob/main/OLED%20Display/main.py) file)

## Run the code:
save the code to the pico and run it and you will how see the string ```Hello World!``` printed onto the display
