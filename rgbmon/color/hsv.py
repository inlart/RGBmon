import core.utils


class Color:
    def __init__(self, settings):
        hue = float(settings["hue"]) / 360.
        saturation = float(settings["saturation"]) / 100.
        value = float(settings["value"]) / 100.
        self.color = core.utils.rgb_from_hsv(hue, saturation, value)
        print(self.color)

    def __getitem__(self, _):
        return self.color

    def __len__(self):
        return 1
