import pytest
import json
from rgbmon.effect.fade import Effect


class Backend():
    def get_led_list(self, _):
        return range(10)

@pytest.fixture()
def effect():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00","0000FF"]}')
    backend_config = json.loads('{"leds":[{"type": 1,"mode": "direct"}]}')
    return Effect(config, backend, backend_config)

class TestFade:
    def test_zero(self, effect):
        color_list = effect.convert(0.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 255)
            assert(g == 0)
            assert(b == 0)

    def test_interpolation1(self, effect):
        color_list = effect.convert(25.0)
        for _, color in color_list:
            r, g, b = color
            assert(r > 0 and r < 255)
            assert(g > 0 and g < 255)
            assert(b == 0)

    def test_half(self, effect):
        color_list = effect.convert(50.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 255)
            assert(b == 0)

    def test_interpolation2(self, effect):
        color_list = effect.convert(75.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g > 0 and g < 255)
            assert(b > 0 and b < 255)

    def test_full(self, effect):
        color_list = effect.convert(100.0)
        for _, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 0)
            assert(b == 255)
