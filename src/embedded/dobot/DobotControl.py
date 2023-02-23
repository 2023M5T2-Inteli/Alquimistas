import Dobot

arm = Dobot.Dobot(225, 3, 140, 0)

arm.moveHome()

arm.pickToggle()
arm.moveArmXY(189, 183, 151, 41)
arm.drawLine(200, 183, -10, 41, -150)
arm.moveArmXY(189, 183, 151, 41)
arm.moveHome()
arm.drawLine(302, 0, -10, 0, -100)
arm.rotateTool(90)
arm.moveHome()
arm.moveArmXY(128, -195, 14, 0)
# arm.pickToggle()

arm.disconnect()