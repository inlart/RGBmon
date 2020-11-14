import core.utils
import pyscreenshot as ImageGrab
import time
import threading
import logging


log = logging.getLogger(__name__)

class Color:
    def __init__(self, config):
        self.color = (255, 255, 255)
        self.sleep = 5
        self.step = 100
        if config and "sleep" in config:
            self.sleep = int(config["sleep"])
        if config and "step" in config:
            self.sleep = int(config["step"])
        log.debug("Ambient sleep set to {}".format(self.sleep))
        log.debug("Ambient step set to {}".format(self.step))
        t = threading.Thread(target=self.updateColor)
        t.start()

    def updateColor(self):
        while True:
            image = ImageGrab.grab().getdata()
            color = (0, 0, 0)
            values = 0
            for i in range(0, len(image), self.step):
                pcolor = image[i]
                color = tuple(map(sum, zip(color, pcolor)))
                values += 1
            self.color = tuple(map(lambda c: int(c / values), color))
            log.debug("Ambient color set to {}".format(self.color))
            time.sleep(self.sleep)

    def __getitem__(self, _):
        return self.color

    def __len__(self):
        return 1
