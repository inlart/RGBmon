import pytest
import json
import colorsys
import collections
from rgbmon.effect.rainbow import Effect


class Backend():
    def get_led_list(self, _):
        return range(12)

@pytest.fixture()
def effect():
    backend = Backend()
    config = json.loads('{"leds":[{"type": 1,"mode": "direct"}]}')
    return Effect(config, backend)

class TestRainbow:
    def test_rainbow(self, effect):
        for i in range(0, 100, 1):
            color_list = effect.convert(i)
            hsv_list = []
            for _, color in color_list:
                r, g, b = color
                h, s, v = colorsys.rgb_to_hsv(r/float(255), g/float(255), b/float(255))
                hsv_list.append(h)
            print(hsv_list)
            hsv_sorted = hsv_list.copy()
            hsv_sorted.sort()

            min_index = 0
            for i in range(len(hsv_list)):
                if hsv_list[i] < hsv_list[min_index]:
                    min_index = i
            hsv_deque = collections.deque(hsv_list)
            hsv_deque.rotate(-min_index)

            assert(list(hsv_deque) == hsv_sorted)
