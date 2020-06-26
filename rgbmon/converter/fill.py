import math

import core.utils

class Converter:
    def __init__(self, config, backend):
        # TODO: check if colors == 2
        self.backend = backend
        self.leds = backend.get_led_list(config["leds"])
        self.default = core.utils.Color.from_string(config["colors"][0])
        self.filled = core.utils.Color.from_string(config["colors"][1])


    def convert(self, value):
        segment_size = 100.0 / (len(self.leds) - 1)
        segment = math.floor(value / segment_size)

        v = (value - segment_size * segment) / segment_size
        fade = self.filled.interpolate(self.default, v)

        out = []
        for i in range(len(self.leds)):
            data = self.filled
            if i > segment:
                data = self.default
            if i == segment:
                data = fade

            out.append((self.leds[i], data))
        return out
