from machine import Pin
import utime
led = Pin(17, Pin.OUT)
pir = Pin(16, Pin.IN)

while True:
   print(pir.value())
   if pir.value() == 1:
       print("There is a movement")
       led.high()
     
   else:
       print("Waiting for movement")
       led.low()
