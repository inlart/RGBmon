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
        num_segments = len(self.leds)
        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if(segment == num_segments):
            segment = num_segments - 1

        out = []
        for i in range(len(self.leds)):
            data = self.default
            if i == segment:
                data = self.filled

            out.append((self.leds[i], data))
        return out
