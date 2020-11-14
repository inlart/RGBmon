import core.utils
from core.colormanager import ColorManager

def invert(value):
    return 0xFF - value

class Color:
    def __init__(self, settings):
        self.colors = ColorManager(settings["colors"])

    def __getitem__(self, key):
        inverted = map(invert, self.colors[key])
        return inverted

    def __len__(self):
        return len(self.colors)
