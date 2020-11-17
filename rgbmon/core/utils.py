import colorsys
import time

def rgb_from_string(color):
    if color[0] == "#":
        color = color[1:]
    r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b)

def rgb_from_hsv(h,s,v):
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
    return (r, g, b)

def interpolate(start, end, v):
    color = finterpolate(start, end, v)
    return tuple(map(lambda c: int(c), color))

def finterpolate(start, end, v):
    sr, sg, sb = start
    er, eg, eb = end
    r = (sr * (1 - v) + er * v)
    g = (sg * (1 - v) + eg * v)
    b = (sb * (1 - v) + eb * v)
    return (r, g, b)

def current_time():
    return int(round(time.time() * 1000))