import pytest
import json

from rgbmon.color.invert import Color

def isColor(color):
    if not isinstance(color, tuple) or len(color) != 3:
        return False
    for c in color:
        if c < 0 or c > 255:
            return False
    return True


class TestInvert:
    def test_value(self):
        settings = json.loads('{"name": "invert", "colors": ["#112233"]}')
        color = Color(settings)
        assert(len(color) == 1)
        c1 = color[0]
        c2 = color[0]
        assert(isColor(c1))
        assert(isColor(c2))
        assert(c1 == c2)
        r, g, b = c1
        assert(r == 0xEE)
        assert(g == 0xDD)
        assert(b == 0xCC)

    def test_hash(self):
        settings = json.loads('{"name": "invert", "colors": ["331122", "FFEEDD"]}')
        color = Color(settings)
        assert(len(color) == 2)
        c1 = color[0]
        c2 = color[0]
        c3 = color[1]
        c4 = color[1]
        assert(isColor(c1))
        assert(isColor(c2))
        assert(isColor(c3))
        assert(isColor(c4))
        assert(c1 == c2)
        assert(c3 == c4)
        assert(c1 != c3)
        r, g, b = c1
        assert(r == 0xCC)
        assert(g == 0xEE)
        assert(b == 0xDD)

        r, g, b = c3
        assert(r == 0x00)
        assert(g == 0x11)
        assert(b == 0x22)
