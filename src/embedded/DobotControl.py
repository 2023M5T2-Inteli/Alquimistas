import Dobot

arm = Dobot.Dobot(225, 3, 140, 0)

arm.moveHome()

arm.drawLine(200, 183, -30, 41, -150)
arm.moveHome()
arm.drawLine(302, 0, -35, 0, -100)
arm.rotateTool(90)
arm.moveHome()
arm.moveArmXY(128, -195, 14, 0)

arm.disconnect()