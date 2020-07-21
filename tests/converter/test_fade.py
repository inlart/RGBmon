import pytest
import json
from rgbmon.converter.fade import Converter


class Backend():
    def get_led_list(self, _):
        return range(10)

@pytest.fixture()
def converter():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00","0000FF"],"leds":[{"type": 1,"mode": "direct"}]}')
    return Converter(config, backend)

class TestFade:
    def test_zero(self, converter):
        color_list = converter.convert(0.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 255)
            assert(g == 0)
            assert(b == 0)

    def test_interpolation1(self, converter):
        color_list = converter.convert(25.0)
        for _, color in color_list:
            r, g, b = color
            assert(r > 0 and r < 255)
            assert(g > 0 and g < 255)
            assert(b == 0)

    def test_half(self, converter):
        color_list = converter.convert(50.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 255)
            assert(b == 0)

    def test_interpolation2(self, converter):
        color_list = converter.convert(75.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g > 0 and g < 255)
            assert(b > 0 and b < 255)

    def test_full(self, converter):
        color_list = converter.convert(100.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 0)
            assert(b == 255)
