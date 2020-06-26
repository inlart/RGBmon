class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_string(cls, color):
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        return cls(r, g, b)

    def interpolate(self, other, v):
        r = int((self.r * (1 - v) + other.r * v))
        g = int((self.g * (1 - v) + other.g * v))
        b = int((self.b * (1 - v) + other.b * v))
        return Color(r, g, b)

    def __str__(self):
        return "[" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + "]"
