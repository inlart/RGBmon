import logging
import core.utils
from core.colormanager import ColorManager

log = logging.getLogger(__name__)

class Color:
    def __init__(self, settings):
        self.smoothness = 99.5
        if "smoothness" in settings:
            self.smoothness = settings["smoothness"]
        log.debug("Smoothness set to {}".format(self.smoothness))
        self.colors = ColorManager(settings["colors"])

    def __getitem__(self, key):
        if not hasattr(self, "color"):
            self.color = self.colors[key]
        else:
            v = (100 - self.smoothness) / 100.
            self.color = core.utils.finterpolate(self.color, self.colors[key], v)
        returncolor = tuple(map(lambda c: int(c), self.color))
        return returncolor

    def __len__(self):
        return len(self.colors)
