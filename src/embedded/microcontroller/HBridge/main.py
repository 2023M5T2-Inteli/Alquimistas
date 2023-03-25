from Modules import HBridge, WifiClient
from time import sleep
from machine import Pin

class Components:
    def __init__(self):
        self.HB = HBridge.HBridge(2, 1, 4, 5)

    def start(self):
        self.HB.enable_first_component()

    def stop_eletromagnet(self):
        self.HB.disable_first_component()

class Network:
    def __init__(self):
        self.AP = WifiClient.WifiClient('Alquimistas', '12345678')

    def accessing_network(self):
        self.AP.connect()

network = Network()
components = Components()

led = Pin("LED", Pin.OUT)
led.on()
# network.accessing_network()
# sleep(5)
components.start()
print('passei aqui')
sleep(50) # time to third table
components.stop_eletromagnet()
print("hello stop")
led.off()