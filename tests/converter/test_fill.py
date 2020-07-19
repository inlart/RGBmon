import pytest
import json
from rgbmon.converter.fill import Converter


class Backend():
    def get_led_list(self, _):
        return range(4)

@pytest.fixture()
def converter():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00"],"leds":[{"type": 1,"mode": "direct"}]}')
    return Converter(config, backend)

class TestFade:
    def test_zero(self, converter):
        color_list = converter.convert(0.0)
        for i, color in color_list:
            assert(color.r == 255)
            assert(color.g == 0)
            assert(color.b == 0)

    def test_first(self, converter):
        color_list = converter.convert(10.0)
        for i, color in color_list:
            if i == 0:
                assert(color.r > 0 and color.r < 255)
                assert(color.g > 0 and color.g < 255)
                assert(color.b == 0)
            else:
                assert(color.r == 255)
                assert(color.g == 0)
                assert(color.b == 0)

    def test_second(self, converter):
        color_list = converter.convert(30.0)
        for i, color in color_list:
            if i == 0:
                assert(color.r == 0)
                assert(color.g == 255)
                assert(color.b == 0)
            elif i == 1:
                assert(color.r > 0 and color.r < 255)
                assert(color.g > 0 and color.g < 255)
                assert(color.b == 0)
            else:
                assert(color.r == 255)
                assert(color.g == 0)
                assert(color.b == 0)

    def test_half(self, converter):
        color_list = converter.convert(50.0)
        for i, color in color_list:
            if i < 2:
                assert(color.r == 0)
                assert(color.g == 255)
                assert(color.b == 0)
            else:
                assert(color.r == 255)
                assert(color.g == 0)
                assert(color.b == 0)

    def test_full(self, converter):
        color_list = converter.convert(100.0)
        for i, color in color_list:
            assert(color.r == 0)
            assert(color.g == 255)
            assert(color.b == 0)
