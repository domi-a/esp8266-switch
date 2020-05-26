from machine import Pin
import network
import urequests
import ujson


def getStr(whatever):
    if type(whatever) == bool:
        if whatever == True:
            return "true"
        else:
            return "false"
    elif(isinstance(whatever, (int, float))):
        return str(whatever)
    else:
        return whatever


class MESSAGE:
    def __init__(self, url, headers):
        self.sta = network.WLAN(network.STA_IF)

        # self.sta.connect("network-name", "password") run once - is enough
        self.url = url
        self.headers = headers
        self.sta.active(True)
        self.sta.connect()
        while self.sta.isconnected() == False:
            pass
        print('wifi connected')

    def send(self, payload: dict):
        data = ujson.dumps(payload)
        try:
            res = urequests.post(self.url, data=data, headers=self.headers)
            res.close()
            if (res.status_code == 200):
                print('sending successful')
                return True
            else:
                return False
        except IndexError as ex:
            print('ERROR rest get ----------', ex)
            return False
