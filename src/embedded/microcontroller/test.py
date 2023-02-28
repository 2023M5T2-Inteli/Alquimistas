from machine import Pin
led = Pin("LED", Pin.OUT)
led.on()  # a method instead of setting the value
led.off() # turn it off again.