import pytest
import json
from rgbmon.effect.fill import Effect


class Backend():
    def get_led_list(self, _):
        return range(4)


@pytest.fixture()
def effect():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00"]}')
    backend_config = json.loads('{"leds":[{"type": 1,"mode": "direct"}]}')
    return Effect(config, backend, backend_config)

@pytest.fixture()
def multi_effect():
    backend = Backend()
    config = json.loads('{"colors":["FF0000","00FF00","0000FF"]}')
    backend_config = json.loads('{"leds":[{"type": 1,"mode": "direct"}]}')
    return Effect(config, backend, backend_config)

class TestFill:
    def test_zero(self, effect):
        color_list = effect.convert(0.0)
        for i, color in color_list:
            r, g, b = color
            assert(r == 255)
            assert(g == 0)
            assert(b == 0)

    def test_first(self, effect):
        color_list = effect.convert(10.0)
        for i, color in color_list:
            r, g, b = color
            if i == 0:
                assert(r > 0 and r < 255)
                assert(g > 0 and g < 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_second(self, effect):
        color_list = effect.convert(30.0)
        for i, color in color_list:
            r, g, b = color
            if i == 0:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            elif i == 1:
                assert(r > 0 and r < 255)
                assert(g > 0 and g < 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_half(self, effect):
        color_list = effect.convert(50.0)
        for i, color in color_list:
            r, g, b = color
            if i < 2:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_full(self, effect):
        color_list = effect.convert(100.0)
        for i, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 255)
            assert(b == 0)

    def test_multicolor_zero(self, multi_effect):
        color_list = multi_effect.convert(0.0)
        for i, color in color_list:
            r, g, b = color
            assert(r == 255)
            assert(g == 0)
            assert(b == 0)

    def test_multicolor_quarter(self, multi_effect):
        color_list = multi_effect.convert(25.0)
        for i, color in color_list:
            r, g, b = color
            if i < 2:
                assert(r == 0)
                assert(g == 255)
                assert(b == 0)
            else:
                assert(r == 255)
                assert(g == 0)
                assert(b == 0)

    def test_multicolor_half(self, multi_effect):
        color_list = multi_effect.convert(50.0)
        for i, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 255)
            assert(b == 0)

    def test_multicolor_full(self, multi_effect):
        color_list = multi_effect.convert(100.0)
        for i, color in color_list:
            r, g, b = color
            assert(r == 0)
            assert(g == 0)
            assert(b == 255)
