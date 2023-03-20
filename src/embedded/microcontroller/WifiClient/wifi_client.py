import network
import socket
from time import sleep
from machine import Pin, PWM
import json

pwm = PWM(Pin(0))
pwm.freq(1000)

ssid = 'Inteli-COLLEGE'
password = 'QazWsx@123'
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

connect()