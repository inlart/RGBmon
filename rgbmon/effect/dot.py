import math

import core.utils
from core.colormanager import ColorManager

class Effect:
    def __init__(self, config, backend, backend_config):
        # TODO: check if colors == 2
        self.backend = backend
        self.leds = backend.get_led_list(backend_config)
        self.colors = ColorManager(config["colors"])

    def convert(self, value):
        num_segments = len(self.leds)
        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if(segment == num_segments):
            segment = num_segments - 1

        out = []
        for i in range(len(self.leds)):
            data = self.colors[0]
            if i == segment:
                data = self.colors[1]

            out.append((self.leds[i], data))
        return out
