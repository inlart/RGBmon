import datetime


class Source:
    def __init__(self, _ : dict):
        return

    def get(self) -> float:
        now = datetime.datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        return 100 * (now - midnight).total_seconds() / (60 * 60 * 24)
