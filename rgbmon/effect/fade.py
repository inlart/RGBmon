import math

import core.utils
from core.colormanager import ColorManager


class Effect:
    def __init__(self, config, backend, backend_config):
        # TODO: check if colors > 1
        self.backend = backend
        self.leds = backend.get_led_list(backend_config)
        self.colors = ColorManager(config["colors"])

    def convert(self, value):
        num_segments = len(self.colors) - 1
        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if segment == num_segments:
            segment = num_segments - 1

        start = self.colors[segment]
        end = self.colors[segment + 1]

        v = (value - segment_size * segment) / segment_size
        data = core.utils.interpolate(start, end, v)

        return list(map(lambda c: (c, data), self.leds))
