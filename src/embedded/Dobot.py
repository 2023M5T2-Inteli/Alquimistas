import DobotDllType as DType

CON_STR = {
    DType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    DType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    DType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}

class Dobot():

    def __init__(self, x = 0, y = 0, z = 0, r = 0):
        self.api = DType.load()
        self.x_home = x
        self.y_home = y
        self.z_home = z
        self.r_home = r
        self.connected = False
        self.verifyConnection()


    def __del__(self):
        self.disconnect()


    def verifyConnection(self):
        if(self.connected):
            print("Dobot already connected!")
        else:
            state = DType.ConnectDobot(self.api, "", 115200)[0]
            if(state == DType.DobotConnect.DobotConnect_NoError):
                print("Connect Status: ", CON_STR[state])
                DType.SetQueuedCmdClear(self.api)

                DType.SetHOMEParams(self.api, self.x_home, self.y_home, self.z_home, self.r_home, isQueued=1)
                DType.SetPTPJointParams(self.api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
                DType.SetPTPCommonParams(self.api, 100, 100, isQueued=1)

                DType.SetHOMECmd(self.api, temp=0, isQueued=1)
                self.connected = True
                return self.connected
            else:
                print("Unable to connect")
                print("Connect status:",CON_STR[state])
                return self.connected
            

    def disconnect(self):
        self.moveHome()
        DType.DisconnectDobot(self.api)


    def commandDelay(self, lastIndex):
        DType.SetQueuedCmdStartExec(self.api)
        while lastIndex > DType.GetQueuedCmdCurrentIndex(self.api)[0]:
            DType.dSleep(2000)
        DType.SetQueuedCmdStopExec(self.api)


    def moveArmXY(self,x,y,z):
        lastIndex = DType.SetPTPCmd(self.api, DType.PTPMode.PTPMOVLXYZMode, x, y, z, 0)[0]
        self.commandDelay(lastIndex)


    def moveHome(self):
        lastIndex = DType.SetPTPCmd(self.api, DType.PTPMode.PTPMOVLXYZMode, self.x_home, self.y_home, self.z_home, self.r_home)[0]
        self.commandDelay(lastIndex)
    
    
    def getPos(self):
        (x, y, z, r, j1, j2, j3, j4) = DType.GetPose(self.api)
        print(f"X-Axis: {x}; Y-Axis: {y}; Z-Axis: {z}; R-Axis: {r}")
        print(f"Joint1: {j1}; Joint2: {j2}; Joint3: {j3}; Joint4: {j4};")
        return [x,y,z]
