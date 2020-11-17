import math
import time

import core.utils

class Source:
    def __init__(self, config):
        self.t = config["period"]
        self.start = core.utils.current_time()
        return

    def get(self):
        diff = core.utils.current_time() - self.start
        value = diff % int(self.t * 1000)

        return value / float(self.t * 1000) * 100
