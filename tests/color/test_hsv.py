import pytest
import json

from rgbmon.color.hsv import Color

def isColor(color):
    if not isinstance(color, tuple) or len(color) != 3:
        return False
    for c in color:
        if c < 0 or c > 255:
            return False
    return True


class TestHSV:
    def test_red(self):
        settings = json.loads('{"hue": 0, "saturation": 100, "value": 100}')
        color = Color(settings)
        assert(len(color) == 1)
        c1 = color[0]
        c2 = color[0]
        assert(isColor(c1))
        assert(isColor(c2))
        assert(c1 == c2)
        r, g, b = c1
        assert(r == 0xFF)
        assert(g == 0x0)
        assert(b == 0x0)

    def test_green(self):
        settings = json.loads('{"hue": 120, "saturation": 75, "value": 75}')
        color = Color(settings)
        assert(len(color) == 1)
        c1 = color[0]
        c2 = color[0]
        assert(isColor(c1))
        assert(isColor(c2))
        assert(c1 == c2)
        r, g, b = c1
        assert(r == 0x30)
        assert(g == 0xBF)
        assert(b == 0x30)
