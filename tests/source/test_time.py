import pytest
from freezegun import freeze_time

from rgbmon.source.time import Source


class TestTime:
    @freeze_time("2020-01-01 00:00:00")
    def test_midnight(self):
        source = Source(None)
        value = source.get()
        assert(value == 0)

    @freeze_time("2020-01-01 06:00:00")
    def test_morning(self):
        source = Source(None)
        value = source.get()
        assert(value == 25)

    @freeze_time("2020-01-01 12:00:00")
    def test_noon(self):
        source = Source(None)
        value = source.get()
        assert(value == 50)