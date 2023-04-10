import time
from lib.umqtt.simple import MQTTClient


class MQTT:
    def __init__(self, client_id, server,port, topic):
        self.client_id = client_id
        self.server = server
        self.port = port
        self.topic = topic
        self.client = MQTTClient(client_id=self.client_id,
                                 server=self.server
                                 )

    def connect(self):
        self.client.connect()

    def publish(self, msg):
        self.client.publish(self.topic, msg)
        print("Published: " + str(msg))
        time.sleep(2)

    def set_callback(self, callback_function):
        self.client.set_callback(callback_function)

    def wait_message(self):
        self.client.wait_msg()

    def subscribe(self):
        self.client.subscribe(self.topic)
        print("Subscribed: " + str(self.topic))

    def disconnect(self):
        self.client.disconnect()

    def check_msg(self):
        self.client.check_msg()

# CM = MQTT(
#     client_id=b"henriquemarlon",
#     server=b"3f0dc5167c844b77b7cc1ad73cb41782.s2.eu.hivemq.cloud",
#     port=0,
# )