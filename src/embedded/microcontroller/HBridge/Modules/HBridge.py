from machine import Pin

class HBridge:
    def __init__(self, in1_pin, in2_pin, in3_pin, in4_pin):
        self.IN1 = Pin(in1_pin, Pin.OUT)
        self.IN2 = Pin(in2_pin, Pin.OUT)
        self.IN3 = Pin(in3_pin, Pin.OUT)
        self.IN4 = Pin(in4_pin, Pin.OUT)

    def enable_first_component(self):
        self.IN1.low()
        self.IN2.high()
        print("amigo estou aqui")
        return("First component is on")
    
    def enable_second_component(self):
        self.IN3.high()
        self.IN4.low()
        return("Second component is on")
    
    def enable_all_components(self):
        self.IN1.high()
        self.IN2.low()
        self.IN3.high()
        self.IN4.low()
        return("All components are on")
    
    def disable_first_component(self):
        self.IN1.low()
        self.IN2.low()
        return("First component is off")
    
    def disable_second_component(self):
        self.IN3.low()
        self.IN4.low()
        return("Second component is off")

    def disable_all_components(self):
        self.IN1.low()
        self.IN2.low()
        self.IN3.low()
        self.IN4.low()
        return("All components are off")
    
# HB = Hbridge(2, 1, 4, 5)
