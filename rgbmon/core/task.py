import time
import logging

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
                time.sleep(self.interval)
                value = self.source.get()
                for converter in self.converters:
                    backend = converter.backend
                    backend.apply(converter.convert(value))
        except Exception as e:
            log.error("Execution of task failed with error: {}".format(e))
