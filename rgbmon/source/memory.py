import psutil


class Source:
    def __init__(self, _ : dict):
        return

    def get(self) -> float:
        return psutil.virtual_memory().percent
