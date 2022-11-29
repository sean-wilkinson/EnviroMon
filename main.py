import bme280
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import utime

i2c0 = SoftI2C(scl=Pin(17), sda=Pin(16), freq=400000)
i2c1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=400000)

oled = SSD1306_I2C(128, 32, i2c0)
bme = bme280.BME280(i2c=i2c1)

while True:
    
    t,p,h = bme.values
    
    oled.fill(0)
    oled.text(t, 0, 0)
    oled.text(h, 0, 10)
    oled.text(p, 0, 20)
    oled.show()
    
    utime.sleep(1)
    

