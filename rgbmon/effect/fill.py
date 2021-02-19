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
        num_segments = len(self.colors) - 1

        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if(segment == num_segments):
            segment = num_segments - 1

        value = (value - segment_size * segment) * num_segments
        color0 = self.colors[segment]
        color1 = self.colors[segment + 1]

        num_segments = len(self.leds)
        segment_size = 100.0 / num_segments
        segment = math.floor(value / segment_size)

        if(segment == num_segments):
            segment = num_segments - 1

        v = (value - segment_size * segment) / segment_size
        fade = core.utils.interpolate(color0, color1, v)

        out = []
        for i in range(len(self.leds)):
            data = color1
            if i > segment:
                data = color0
            if i == segment:
                data = fade

            out.append((self.leds[i], data))
        return out
