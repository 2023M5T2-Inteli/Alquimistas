import DobotDllType as DType

CON_STR = {
    DType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    DType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    DType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"
}

api = DType.load()
xHome = 70
yHome = 70
zHome = 70
rHome = 50

state = DType.ConnectDobot(api, "", 115200)[0]

if(state == DType.DobotConnect.DobotConnect_NoError):
    print("Connect Status: ", CON_STR[state])
    DType.SetQueuedCmdClear(api)

    DType.SetHOMEParams(api, xHome, yHome, zHome, rHome, isQueued=1)
    DType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1) #Setta a velocidade e a aceleração de cada articulação
    DType.SetPTPCommonParams(api, 100, 100, isQueued=1) #Setta parametros comuns às juntas

    DType.SetHOMECmd(api, temp = 0, isQueued = 1)

    lastIndex = DType.SetPTPCmd(api, DType.PTPMode.PTPMOVLXYZMode, xHome, yHome, zHome, rHome, isQueued=1)[0]

    DType.SetQueuedCmdStartExec(api)

    while lastIndex > DType.GetQueuedCmdCurrentIndex(api)[0]:
        DType.dSleep(100)
        print(lastIndex)

    DType.SetQueuedCmdStopExec(api)



DType.DisconnectDobot(api)

print('YAY!')