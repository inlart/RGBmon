import time
import logging

log = logging.getLogger(__name__)

class Task:
    def __init__(self, interval, source, converters):
        self.interval = interval
        self.source = source
        self.converters = converters

    def run(self):
        try:
            while True:
                time.sleep(self.interval)
                value = self.source.get()
                for converter in self.converters:
                    backend = converter.backend
                    backend.apply(converter.convert(value))
        except Exception as e:
            log.error("Execution of task failed with error: {}".format(e))
