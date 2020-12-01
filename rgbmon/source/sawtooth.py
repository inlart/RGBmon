import core.utils


class Source:
    def __init__(self, config : dict):
        self.t = config["period"]
        self.start = core.utils.current_time()
        return

    def get(self) -> float:
        diff = core.utils.current_time() - self.start
        value = diff % int(self.t * 1000)

        return value / float(self.t * 1000) * 100
