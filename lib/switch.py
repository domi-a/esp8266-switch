from machine import Pin


def arr_count(arr):
    i = 0
    count = 0
    while i < len(arr):
        count += arr[i]
        i += 1
    return count


def bool_arr(count):
    arr = []
    i = 0
    while i < count:
        arr.append(False)
        i += 1
    return arr


class SWITCH:
    def __init__(self, pin, history_size):
        self.history_size = history_size
        self.switch = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.prev_swtich_value = self.switch.value()
        self.changes_history = bool_arr(history_size)
        self.click_count = 0
        self.click = False

    def update(self):
        self.change = self.switch.value() != self.prev_swtich_value
        self.prev_swtich_value = self.switch.value()

        if self.changes_history[0]:
            self.click_count = arr_count(self.changes_history)
            # print('click', self.click_count, self.changes_history)
            self.changes_history = bool_arr(self.history_size)
            self.click = True
        else:
            self.click = False

        self.changes_history.append(self.change)
        del self.changes_history[0]

    def clicks(self):
        if self.click:
            return self.click_count
        else:
            return 0
