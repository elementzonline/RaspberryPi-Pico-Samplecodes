from machine import Pin
import utime

led1 = Pin(13, Pin.OUT) # GPIO pin 13 of pico board #
led2 = Pin(14, Pin.OUT) # GPIO pin 14 of pico board #
led3 = Pin(15, Pin.OUT) # GPIO pin 15 of pico board #

while True:

    led1.value(1) #To turn ON led #
    utime.sleep(1)
    led1.value(0) #To turn OFF led #
    led2.value(1)
    utime.sleep(1)
    led2.value(0)
    led3.value(1)
    utime.sleep(1)
    led3.value(0)

