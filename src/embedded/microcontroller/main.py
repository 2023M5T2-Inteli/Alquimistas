from machine import Pin
from time import sleep

class Componentes:
    def __init__(self, in1_pin, in2_pin, in3_pin, in4_pin, button1_pin, button2_pin):
        self.IN1 = Pin(in1_pin, Pin.OUT)
        self.IN2 = Pin(in2_pin, Pin.OUT)
        self.IN3 = Pin(in3_pin, Pin.OUT)
        self.IN4 = Pin(in4_pin, Pin.OUT)
        self.Button1 = Pin(button1_pin, Pin.IN)
        self.Button2 = Pin(button2_pin, Pin.IN)

    def ligar_componentes(self):
        if self.Button1.value() == 1:
            self.IN1.high()
            self.IN2.low()
            print("Componentes ligados")
        else:
            self.IN1.low()
            self.IN2.low()
            print("Componentes desligados")

componentes = Componentes(0, 1, 4, 5, 15, 17)

while True:
    sleep(2)
    componentes.ligar_componentes()
    print(Pin(15).value())