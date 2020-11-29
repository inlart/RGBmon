import pytest
import json

from rgbmon.color.random import Color


def isColor(color):
    if not isinstance(color, tuple) or len(color) != 3:
        return False
    for c in color:
        if c < 0 or c > 255:
            return False
    return True


class TestRandom:
    def test_random(self):
        for i in range(100):
            settings = json.loads('{"name": "random"}')
            color = Color(settings)
            assert(len(color) == 1)
            c1 = color[0]
            assert(isColor(c1))
            r, g, b = c1
            assert(r >= 0x00 and r <= 0xFF)
            assert(g >= 0x00 and g <= 0xFF)
            assert(b >= 0x00 and b <= 0xFF)
