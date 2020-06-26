import psutil

class Source:
    def __init__(self, _):
        return

    def get(self):
        return psutil.virtual_memory().percent
