from serial.tools import list_ports
import pydobot
# Checking ports of your computer
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')

# Instance of your dobot connection
device = pydobot.Dobot(port='COM3', verbose=True)
# Defining home
device_home = device.pose()

# device_position = device.pose()
(xHome, yHome, zHome, rHome) = [200, -5, 150, 0]
#Bandeja 1:  [278, 193, -33, 36] -> [128, 182, -40, 56] -> [134, 191, 150, 56]
#Bandeja 2:  [323, -14, -44, -4] -> [167, -9, -12, -5] -> [134, 191, 150, 56]
#Bandeja 3: [213, -202, -24, -44] -> 

device.pose()

# Primeiro movimento (max "x")
# Primeira Bandeija
device.move_to(xHome, yHome, zHome, rHome, wait=True)
# device.move_to(193, 212, -43, 47, wait=True)
# device.move_to(32, 217, -34, 81, wait=True)
# device.move_to(48, 217, 116, 75, wait=True)
# device.move_to(xHome, yHome, zHome, rHome, wait=True)

# # Segunda Bandeija
# device.move_to(323, -14, -44, -4, wait=True)
# device.move_to(167, -9, -12, -5, wait=True)
# device.move_to(190, 4, 87, 1, wait=True)
# # device.pose()

# # Terceira Bandeija
# device.move_to(90, -179, 114, -63, wait=True)
# device.move_to(129, -196, -40, -57, wait=True)
# device.move_to(90, -179, 114, -63, wait=True)
# device.move_to(xHome, yHome, zHome, rHome, wait=True)
# device.pose()

# device_position = device.pose()
device.close()

print('YAY!')