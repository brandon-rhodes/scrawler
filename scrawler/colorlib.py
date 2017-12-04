
black = (0.0, 0.0, 0.0, 1.0)

# def to_rgb(color):
#     color = color.lstrip('#')
#     return (int(color[0], 16) / 15.0,
#             int(color[1], 16) / 15.0,
#             int(color[2], 16) / 15.0)

def blend(fraction, color1, color2):
    r1, g1, b1 = to_rgb(color1)
    r2, g2, b2 = to_rgb(color2)
    return (r1 + (r2 - r1) * fraction,
            g1 + (g2 - g1) * fraction,
            b1 + (b2 - b1) * fraction)
