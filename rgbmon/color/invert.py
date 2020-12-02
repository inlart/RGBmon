from core.colormanager import ColorManager


def invert(value : int) -> int:
    return 0xFF - value


class Color:
    def __init__(self, settings : dict):
        self.colors = ColorManager(settings["colors"])

    def __getitem__(self, key : int) -> tuple[int, int, int]:
        inverted = tuple(map(invert, self.colors[key]))
        return inverted

    def __len__(self) -> int:
        return len(self.colors)
