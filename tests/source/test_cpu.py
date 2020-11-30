import pytest

from rgbmon.source.cpu import Source


class TestCPU:
    def test_range(self):
        source = Source(None)
        for i in range(100):
            value = source.get()
            assert(value >= 0 and value <= 100)
