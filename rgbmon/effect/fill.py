import math

import core.utils

class Effect:
    def __init__(self, config, backend, backend_config):
        # TODO: check if colors == 2
        self.backend = backend
        self.leds = backend.get_led_list(backend_config)
        self.default = core.utils.rgb_from_string(config["colors"][0])
        self.filled = core.utils.rgb_from_string(config["colors"][1])


    def convert(self, value):
        num_segments = len(self.leds)
        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if(segment == num_segments):
            segment = num_segments - 1

        v = (value - segment_size * segment) / segment_size
        fade = core.utils.interpolate(self.default, self.filled, v)

        out = []
        for i in range(len(self.leds)):
            data = self.filled
            if i > segment:
                data = self.default
            if i == segment:
                data = fade

            out.append((self.leds[i], data))
        return out
