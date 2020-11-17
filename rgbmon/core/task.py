import time
import logging

import core.utils

log = logging.getLogger(__name__)

class Task:
    def __init__(self, interval, source, converters):
        self.interval = interval
        self.source = source
        self.converters = converters
        self.keepRunning = True

    def stop(self):
        self.keepRunning = False

    def run(self):
        try:
            while self.keepRunning:
                startTime = core.utils.current_time()
                value = self.source.get()
                for converter in self.converters:
                    backend = converter.backend
                    backend.apply(converter.convert(value))
                sleepTime = self.interval - (core.utils.current_time() - startTime) / 1000.
                if sleepTime > 0:
                    time.sleep(sleepTime)
                else:
                    log.warning("Missed task execution by {}s - consider increasing the task interval".format(abs(sleepTime - self.interval)))
        except Exception as e:
            log.error("Execution of task failed with error: {}".format(e))
