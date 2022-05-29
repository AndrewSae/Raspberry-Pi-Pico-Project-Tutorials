from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

width = 128
height = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16))
oled = SSD1306_I2C(width, height, i2c)

oled.fill(0)
oled.text("hello",0,0)
oled.text("from pi",0,10)
oled.text("pico",0,20)
oled.show()


