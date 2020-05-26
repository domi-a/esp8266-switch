
from machine import Pin
import utime
from main.lib.rest_message import MESSAGE
from main.lib.switch import SWITCH
from main.lib.environment import ENVIRONMENT
from main.lib.mqtt_message import MQTT_MESSAGE


class SWITCH_MAIN:
    def __init__(self):
        print('start switch main ...')
        env = ENVIRONMENT('env')

        self.mqtt_client = MQTT_MESSAGE(env.read('mqtt'))

        self.led = Pin(2, mode=Pin.OUT, pull=None)
        self.s1 = SWITCH(14, 1)
        self.s2 = SWITCH(12, 15)
        self.led.on()  # off

    def blink(self, blinksLeft, ms_duration):
        while(blinksLeft > 0):
            blinksLeft = blinksLeft - 1
            self.led.off()  # on
            utime.sleep_ms(ms_duration)
            self.led.on()  # off
            utime.sleep_ms(ms_duration)

    def main_work(self):
        self.s1.update()
        self.s2.update()
        payload = dict()
        payload['light'] = 'wifi_1'
        if self.s1.clicks() or self.s2.clicks():
            clicks = s1.clicks() + s2.clicks()
            print(clicks, 'clicks')
            payload['clicks'] = clicks
            mqtt_client.send('switch/wifi_switch_1', payload)
            self.blink(clicks, 100)

    def main_loop(self, update_ms):
        while True:
            self.main_work()
            utime.sleep_ms(update_ms)
