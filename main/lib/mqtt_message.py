
from umqtt.robust import MQTTClient
import ubinascii
import machine
import network
import json
import utime


class MQTT_MESSAGE:
    def __init__(self, server):
        self.station = network.WLAN(network.STA_IF)
        # self.station.ifconfig(
        #     ('192.168.3.201', '255.255.255.0', '192.168.3.1', '192.168.3.1'))
        self.server = server
        self.station.active(True)
        self.station.connect()
        while self.station.isconnected() == False:
            pass
        print('wifi connected')
        client_id = ubinascii.hexlify(machine.unique_id())+'-bbb'
        print(client_id, self.server)

        self.client = MQTTClient(client_id, self.server)
        self.client.connect()
        print('mqtt connected')

    def restart_and_reconnect():
        print('Failed to connect to MQTT broker. Reconnecting...')
        utime.sleep(10)
        machine.reset()

    def send(self, topic, payload):

        try:

            self.client.publish(topic, json.dumps(payload))
            # client.disconnect()
            print('message sent')
        except OSError as e:
            client.disconnect()
            restart_and_reconnect()
        except:
            client.disconnect()
