import math
import time

def current_time():
    return int(round(time.time() * 1000))

class Source:
    def __init__(self, config):
        self.t = config["period"]
        self.start = current_time()
        return

    def get(self):
        diff = current_time() - self.start
        value = diff % int(self.t * 1000)

        return value / float(self.t * 1000) * 100
