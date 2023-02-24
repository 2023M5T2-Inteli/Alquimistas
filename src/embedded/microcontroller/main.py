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
        IN3.high()
        IN4.low()
        print("Ligar Lado 1")
        
    elif Button2.value() == 1:
        IN1.low()
        IN2.high()
        IN3.low()
        IN4.high()
        print("Ligar Lado 2")

    else:
        IN1.low()
        IN2.low()
        print("Desligar tudo")
