from machine import Pin
from time import sleep
led = Pin("LED", Pin.OUT)

led.on()
sleep(1)
led.off()
sleep(1)
led.on()
  # a method instead of setting the value
#led.off() # turn it off again.