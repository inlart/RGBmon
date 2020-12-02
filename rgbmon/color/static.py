from typing import Tuple

import core.utils


class Color:
    def __init__(self, settings : dict):
        self.value = core.utils.rgb_from_string(settings["value"])

    def __getitem__(self, _ : int) -> Tuple[int, int, int]:
        return self.value

    def __len__(self) -> int:
        return 1
