import machine
import socket
import network
import time
import math


in1 = machine.Pin(0, machine.Pin.OUT)
in2 = machine.Pin(1, machine.Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Inteli-COLLEGE", "QazWsx@123")

print('Connecting')

wait = 10

while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('.')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('WiFi connection failed')
else:
    print('Connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)

def server(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass

        print(request)
        
        if(request == '/ON'):
            in1.low()
            in2.high()
            client.send('ON')
        elif (request == '/OFF'):
            in1.high()
            in2.low()
            client.send('OFF')
        elif (request == '/STOP'):
            in1.low()
            in2.low()
            client.send('STOP')
        else:
            pass
        
        client.close()

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection

try:
    if ip is not None:
        connection=open_socket(ip)
        server(connection)
except KeyboardInterrupt:
    machine.reset()

