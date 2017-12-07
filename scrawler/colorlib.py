
black = (0.0, 0.0, 0.0, 1.0)
white = (1.0, 1.0, 1.0, 1.0)

def apply_alpha(color_plus_alpha, color):
    r1, g1, b1, a = color_plus_alpha
    if a == 1.0:
        return r1, g1, b1
    r2, g2, b2 = color
    return (r2 + (r1 - r2) * a,
            g2 + (g1 - g2) * a,
            b2 + (b1 - b2) * a)

def rgb_color(string):
    """Convert an RGB color string to an RGB tuple.

    >>> c = rgb_color
    >>> c('#fff')
    (1.0, 1.0, 1.0)
    >>> c('#FFA500')
    (1.0, 0.6470588235294118, 0.0)

    """
    string = string.lstrip('#')
    if len(string) == 3:
        return (int(string[0], 16) / 15.0,
                int(string[1], 16) / 15.0,
                int(string[2], 16) / 15.0)
    elif len(string) == 6:
        return (int(string[0:2], 16) / 255.0,
                int(string[2:4], 16) / 255.0,
                int(string[4:6], 16) / 255.0)
    else:
        raise ValueError('RGB color strings must have 3 or 6 digits,'
                         ' unlike {!r}'.format(string))
