import network

class SoftAP:
    def __init__(self, ssid, password, security):
        self.ssid = ssid
        self.password = password
        self.security = security
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid=self.ssid, password=self.password, security=self.security)

    def start_access_point(self):
        self.ap.active(True)
        config = self.ap.ifconfig()
        print(f'Connected on {config}')
        return(config)

# AP = SoftAP('Alquimistas', '12345678', 4)
