import pytest
import json
from rgbmon.converter.dot import Converter


class Backend():
    def get_led_list(self, _):
        return range(4)

@pytest.fixture()
def converter():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00"],"leds":[{"type": 1,"mode": "direct"}]}')
    return Converter(config, backend)

class TestDot:
    def test_zero(self, converter):
        color_list = converter.convert(0.0)
        for i, color in color_list:
            r, g, b = color
            if i == 0:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_first(self, converter):
        color_list = converter.convert(10.0)
        for i, color in color_list:
            r, g, b = color
            if i == 0:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_second(self, converter):
        color_list = converter.convert(30.0)
        for i, color in color_list:
            r, g, b = color
            if i == 1:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_half(self, converter):
        color_list = converter.convert(50.0)
        for i, color in color_list:
            r, g, b = color
            if i == 2:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_full(self, converter):
        color_list = converter.convert(100.0)
        for i, color in color_list:
            r, g, b = color
            if i == 3:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)
