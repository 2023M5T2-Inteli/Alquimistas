from machine import Pin
from time import sleep

IN1 = Pin(0, Pin.OUT)
IN2 = Pin(1, Pin.OUT)
IN3 = Pin(2, Pin.OUT)
IN4 = Pin(3, Pin.OUT)

Button1 = Pin(16, Pin.IN)
Button2 = Pin(17, Pin.IN)

while True:
    sleep(2)
    if Button1.value() == 1:
        IN1.high()
        IN2.low()
        print("Componentes ligados")
        
    elif Button2.value() == 1:
        IN1.low()
        IN2.high()
        print("Componentes ligados")

    else:
        IN1.low()
        IN2.low()
        print("Componentes desligados")
