import math

import core.utils

class Effect:
    def __init__(self, config, backend, backend_config):
        self.backend = backend
        self.leds = backend.get_led_list(backend_config)

    def convert(self, value):
        num_segments = len(self.leds)
        segment_size = 1.0 / num_segments
        offset = value / 100

        out = []
        for i in range(len(self.leds)):
            value = offset + i * segment_size
            if value > 1.0:
                value -= 1.0
            data = core.utils.rgb_from_hsv(value, 1, 1)

            out.append((self.leds[i], data))
        return out
