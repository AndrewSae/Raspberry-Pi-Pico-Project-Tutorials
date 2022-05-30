from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

width = 128
height = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16))
oled = SSD1306_I2C(width, height, i2c)

oled.fill(0)
oled.text("Hello World!", 0,0)
oled.show()
