import colorsys

def rgb_from_string(color):
    r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
    return (r, g, b)

def rgb_from_hsv(h,s,v):
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
    return (r, g, b)

def interpolate(start, end, v):
    sr, sg, sb = start
    er, eg, eb = end
    r = int((sr * (1 - v) + er * v))
    g = int((sg * (1 - v) + eg * v))
    b = int((sb * (1 - v) + eb * v))
    return (r, g, b)
