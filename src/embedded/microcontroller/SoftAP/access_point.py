#imports
try:
 import usocket as socket
except:
 import socket
import network
import gc

#Wifi configurations
gc.collect()
ssid = 'Alquimistas'
password = '12345678'

#Defining WLAN configurations
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

while ap.active() == False:
  pass
print('Conectado')
print(ap.ifconfig()) #Print running port

#Creating web-page
def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
  <body><h1>Funcionou porra!!</h1></body></html>"""
  return html

#Defining port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Pegando a conexão do %s' % str(addr))
  request = conn.recv(1024)
  print(' = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()