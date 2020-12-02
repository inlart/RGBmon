import core.utils


class Color:
    def __init__(self, settings : dict):
        hue = float(settings["hue"]) / 360.
        saturation = float(settings["saturation"]) / 100.
        value = float(settings["value"]) / 100.
        self.color = core.utils.rgb_from_hsv(hue, saturation, value)

    def __getitem__(self, _ : int) -> tuple[int, int, int]:
        return self.color

    def __len__(self) -> int:
        return 1
