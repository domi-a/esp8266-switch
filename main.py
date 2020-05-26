
from main.ota_updater import OTAUpdater
from main.switch_main import SWITCH_MAIN
import utime
from main.lib.environment import ENVIRONMENT
from machine import Pin

led = Pin(2, mode=Pin.OUT, pull=None)
led.on()  # off


def blink(blinksLeft, ms_duration):
    while(blinksLeft > 0):
        blinksLeft = blinksLeft - 1
        led.off()  # on
        utime.sleep_ms(ms_duration)
        led.on()  # off
        utime.sleep_ms(ms_duration)


def download_and_install_update_if_available():
    env = ENVIRONMENT('env')
    blink(2, 200)
    ota_updater = OTAUpdater(env.read('giturl'))
    update_available = ota_updater.download_and_install_update_if_available(
        env.read('ssid'), env.read('wifi-pw'))
    if update_available:
        blink(5, 50)


def start():
    switch = SWITCH_MAIN()
    switch.main_loop(21)


def boot():
    download_and_install_update_if_available()
    start()


boot()
