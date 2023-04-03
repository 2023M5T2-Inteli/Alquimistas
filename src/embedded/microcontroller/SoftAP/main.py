from Modules import SoftAP
from time import sleep
from machine import Pin

class Network:
    def __init__(self):
        self.AP = SoftAP.SoftAP('Alquimistas', '12345678', 4)

    def access_point(self):
        self.AP.start_access_point()


network = Network()
while True:
    try:
        led = Pin("LED", Pin.OUT)
        led.on()  # a method instead of setting the value
        # led.off() # turn it off again.
        network.access_point()
        sleep(5)
    except Exception as e:
        print(e)