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
        value = diff / float(self.t * 1000)

        return 50 * math.sin(2 * math.pi * value) + 50
