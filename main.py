
from machine import Pin
import utime
from rest_message import MESSAGE
from switch import SWITCH
from environment import ENVIRONMENT
from mqtt_message import MQTT_MESSAGE

print('start ...')
env = ENVIRONMENT('env')
# rest_client = MESSAGE(env.read('url'), {
#                       'Content-Type': 'application/json', 'Authorization': env.read('Authorization')})
mqtt_client = MQTT_MESSAGE(env.read('mqtt'))

led = Pin(2, mode=Pin.OUT, pull=None)
s1 = SWITCH(14, 1)


s2 = SWITCH(12, 15)
update_ms = 20
led.on()  # off


def blink(blinksLeft, ms_duration):
    while(blinksLeft > 0):
        blinksLeft = blinksLeft - 1
        led.off()  # on
        utime.sleep_ms(ms_duration)
        led.on()  # off
        utime.sleep_ms(ms_duration)


def main_work():
    s1.update()
    s2.update()
    payload = dict()
    payload['light'] = 'wifi_1'
    if s1.clicks() or s2.clicks():
        clicks = s1.clicks() + s2.clicks()
        print(clicks, 'clicks')
        payload['clicks'] = clicks
        mqtt_client.send('switch/wifi_test', payload)
        # sendOk = rest_client.send(payload)
        blink(clicks, 100)


while True:
    main_work()
    utime.sleep_ms(update_ms)
