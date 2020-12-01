import psutil


class Source:
    def __init__(self, _ : dict):
        return

    def get(self) -> float:
        return psutil.cpu_percent()
