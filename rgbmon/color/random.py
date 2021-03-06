import random
import logging
from typing import Tuple

import core.utils

log = logging.getLogger(__name__)


def randomColor() -> Tuple[int, int, int]:
    return tuple([random.randint(0, 0xff) for i in range(3)])


class Color:
    def __init__(self, settings : dict):
        self.interval = 1000
        self.colorSize = 1
        if settings and "interval" in settings:
            self.interval = settings["interval"]
        if settings and "size" in settings:
            self.colorSize = settings["size"]
        log.debug("Random color interval set to {}".format(self.interval))
        log.debug("Random color size set to {}".format(self.colorSize))
        self.setValue()

    def setValue(self):
        self.lastUpdate = core.utils.current_time()
        self.value = [randomColor() for i in range(self.colorSize)]

    def __getitem__(self, key : int) -> Tuple[int, int, int]:
        if core.utils.current_time() - self.lastUpdate > self.interval:
            self.setValue()
        return self.value[key]

    def __len__(self) -> int:
        return self.colorSize
