#imports
try:
 import usocket as socket
except:
 import socket
import network
import gc
import time
from hbridge import hbridge
# Ideia para encapsular o código de AP e rodar ao mesmo tempo que rodamos a funcão de eletroimã.
import multiprocessing

#Wifi configurations
gc.collect()
ssid = 'Alquimistas1'
password = '12345678'
security = 4

#Defining WLAN configurations
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password, security=security)
ap.active(True)

componentes = hbridge.Componentes(0, 1, 4, 5, 15, 17)

while ap.active() == False:
  pass
print('Conectado')
print(ap.ifconfig()) #Print running port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Pegando a conexão do %s' % str(addr))
  request = conn.recv(1024)
  print(' = %s' % str(request))
  response = componentes.enable_eletromagnet()
  conn.send(response)
  conn.close()