import core.color
from functools import reduce


class ColorManager:
    def __init__(self, config):
        self.colors = []
        for color_config in config:
            self.colors.append(core.color.load_color(color_config))
        self.length = reduce(lambda count, l: count + len(l), self.colors, 0)

    def __getitem__(self, key):
        cur = 0
        for color in self.colors:
            cur_len = len(color)
            if cur + cur_len > key:
                return color[key - cur]
            cur = cur + cur_len
        return None

    def __len__(self):
        return self.length
