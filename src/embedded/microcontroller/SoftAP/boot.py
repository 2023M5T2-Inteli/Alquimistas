from time import sleep
from machine import Pin
from Modules import soft_ap

class Network:
    def __init__(self):
        self.AP = soft_ap.SoftAP('Alquimistas', '12345678', 4)

network = Network()

if __name__ == '__main__':
    while True:
        try:
            led = Pin("LED", Pin.OUT)
            led.on() 
            network.AP.start_access_point()
            sleep(5)
        except Exception as e:
            print(e)