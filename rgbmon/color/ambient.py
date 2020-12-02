import pyscreenshot as ImageGrab
import time
import threading
import logging


log = logging.getLogger(__name__)

updateThread = None
updateColors = []


def updateColor(step : int, sleep : int):
    while True:
        image = ImageGrab.grab().getdata()
        color = (0, 0, 0)
        values = 0
        for i in range(0, len(image), step):
            pcolor = image[i]
            color = tuple(map(sum, zip(color, pcolor)))
            values += 1
        color = tuple(map(lambda c: int(c / values), color))
        log.debug("Ambient color set to {} in {} modules".format(color, len(updateColors)))
        for c in updateColors:
            c.setColor(color)
        time.sleep(sleep)


class Color:
    def __init__(self, config : dict):
        global updateThread
        global updateColors
        self.color = (255, 255, 255)
        self.sleep = 5
        self.step = 100
        if config and "sleep" in config:
            self.sleep = int(config["sleep"])
        if config and "step" in config:
            self.sleep = int(config["step"])
        log.debug("Ambient sleep set to {}".format(self.sleep))
        log.debug("Ambient step set to {}".format(self.step))
        updateColors.append(self)
        if not updateThread:
            log.debug("Starting ambient update thread with step {} and sleep {}".format(self.step, self.sleep))
            updateThread = threading.Thread(target=updateColor, args=[self.step, self.sleep])
            updateThread.start()

    def setColor(self, color : tuple[int, int, int]):
        self.color = color

    def __getitem__(self, _ : int) -> tuple[int, int, int]:
        return self.color

    def __len__(self) -> int:
        return 1
