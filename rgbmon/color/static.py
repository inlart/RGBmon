import core.utils


class Color:
    def __init__(self, settings):
        self.value = core.utils.rgb_from_string(settings["value"])

    def __getitem__(self, _):
        return self.value

    def __len__(self):
        return 1
