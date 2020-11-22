import pytest
import rgbmon.core.utils


class TestUtils:
    def test_rgb_from_string(self):
        r, g, b = rgbmon.core.utils.rgb_from_string("112233")
        assert(r == 0x11)
        assert(g == 0x22)
        assert(b == 0x33)
        r, g, b = rgbmon.core.utils.rgb_from_string("#112233")
        assert(r == 0x11)
        assert(g == 0x22)
        assert(b == 0x33)

    def test_rgb_from_hsv(self):
        r, g, b = rgbmon.core.utils.rgb_from_hsv(60 / 360., 1, 1)
        assert(r == 0xFF)
        assert(g == 0xFF)
        assert(b == 0x0)
        r, g, b = rgbmon.core.utils.rgb_from_hsv(0, 1, 1)
        assert(r == 0xFF)
        assert(g == 0x0)
        assert(b == 0x0)
        r, g, b = rgbmon.core.utils.rgb_from_hsv(0, 0, 0.75)
        assert(r == 0xBF)
        assert(g == 0xBF)
        assert(b == 0xBF)

    def test_interpolate(self):
        start = (0xFF, 0x0 , 0x0)
        end = (0x0, 0x0 , 0x0FF)
        r, g, b = rgbmon.core.utils.interpolate(start, end, 0)
        assert(r == 0xFF)
        assert(g == 0x0)
        assert(b == 0x0)
        r, g, b = rgbmon.core.utils.interpolate(start, end, 1)
        assert(r == 0x0)
        assert(g == 0x0)
        assert(b == 0xFF)
        r, g, b = rgbmon.core.utils.interpolate(start, end, 0.5)
        assert(r == 0x7F)
        assert(g == 0x0)
        assert(b == 0x7F)

    def test_current_time(self):
        cur = rgbmon.core.utils.current_time()
        for i in range(10):
            newTime = rgbmon.core.utils.current_time()
            assert(cur >= newTime)
            cur = newTime
