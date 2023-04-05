from machine import Pin, ADC
import utime

# magnetic sensor sensitivity (mV/Gauss)
sensitivity = 1.6

# ADC0 pin for analog voltage reading
adc = machine.ADC(0)

# GPIO5 pin for digital signal reading
hall_sensor = machine.Pin(5, machine.Pin.IN)

while True:
    # read the analog voltage on pin ADC0 and print the value
    analog_value = adc.read_u16()
    print("Tensão analógica: ", analog_value)

    # calculate the magnetic field in Gauss
    valor_campo = analog_value / sensitivity
    print("Campo magnético: ", campo_magnetico, "Gauss")

    campo_magnetico = valor_campo * 50.65 * e^-6 * 1.6

# min = 800G
# max = 12 KG
    utime.sleep(5)
    
# a sensibilidade do módulo sensor magnético FE01 é de 1.6 mV/Gauss
# para calcular o campo magnético em Gauss, precisa dividir a tensão analógica lida
# pelo valor da sensibilidade.



