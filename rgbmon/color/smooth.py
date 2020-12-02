import logging
from typing import Tuple

import core.utils
from core.colormanager import ColorManager

log = logging.getLogger(__name__)


class Color:
    def __init__(self, settings : dict):
        self.smoothness = 99.5
        if "smoothness" in settings:
            self.smoothness = settings["smoothness"]
        log.debug("Smoothness set to {}".format(self.smoothness))
        self.colors = ColorManager(settings["colors"])
        self.color = [None] * len(self.colors)

    def __getitem__(self, key : int) -> Tuple[int, int, int]:
        if not self.color[key]:
            self.color[key] = self.colors[key]
        else:
            v = (100 - self.smoothness) / 100.
            self.color[key] = core.utils.finterpolate(self.color[key], self.colors[key], v)
        returncolor = tuple(map(lambda c: int(c), self.color[key]))
        return returncolor

    def __len__(self) -> int:
        return len(self.colors)
