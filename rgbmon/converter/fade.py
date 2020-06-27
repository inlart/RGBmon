import math

import core.utils


class Converter:
    def __init__(self, config, backend):
        # TODO: check if colors > 1
        self.backend = backend
        self.leds = backend.get_led_list(config["leds"])
        self.colors = list(map(lambda c: core.utils.Color.from_string(c), config["colors"]))

    def convert(self, value):
        segment_size = 100.0 / (len(self.colors) - 1)
        segment = math.floor(value / segment_size)
        if segment >= segment_size:
            segment = segment_size - 1

        start = self.colors[segment]
        end = self.colors[segment + 1]

        v = (value - segment_size * segment) / segment_size
        data = start.interpolate(end, v)

        return list(map(lambda c: (c, data), self.leds))
