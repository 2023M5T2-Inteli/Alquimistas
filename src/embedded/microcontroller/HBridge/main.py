from Modules import h_bridge, mqtt_client


class Components:
    def __init__(self):
        self.MC = mqtt_client.MQTT(
            client_id="henriquemarlon",
            server="192.168.4.17",
            port=1883,
            topic="response"
        )
        self.HB = h_bridge.HBridge(2, 1)

    def routine(self):
        def callback(topic, msg):
            response = int(msg.decode("utf-8"))
            print(response)
            if response == 1:
                self.HB.enable_first_component()

            elif response == 0:
                self.HB.disable_first_component()

        self.MC.set_callback(callback)
        self.MC.connect()
        print("Connected to MQTT Broker")
        self.MC.subscribe()

        while True:
            self.MC.wait_message()


MW = Components()

if __name__ == '__main__':
    while True:
        MW.routine()
