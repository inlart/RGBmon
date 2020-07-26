import psutil

class Source:
    def __init__(self, config):
        self.entry = config["entry"]
        self.label = config["label"]
        self.min = 20.0
        self.max = 100.0
        if "min" in config:
            self.min = config["min"]
        if "max" in config:
            self.max = config["max"]
        return

    def get(self):
        temps = psutil.sensors_temperatures()
        if self.entry not in temps:
            raise RuntimeError("Could not find temerature entry {}".format(self.entry))

        entry = temps[self.entry]
        for temp in entry:
            if temp.label != self.label:
                continue
            value = (temp.current - self.min) * 100.0 / (self.max - self.min)
            return max(min(value, 100.0), 0.0)

        raise RuntimeError("Could not find temerature label {}".format(self.label))