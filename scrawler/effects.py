"""Visual effects."""

#from .colorlib import blend

def fade_in(animation, duration):

    if duration > 2:
        denominator = duration - 1.0
        alphas = [i / denominator for i in range(duration)]
    elif duration == 2:
        alphas = 0.0, 1.0
    else:
        alphas = 1.0,

    for alpha, frame in zip(alphas, animation):
        yield [(x, y, text, (fg[0], fg[1], fg[2], fg[3] * alpha), bg)
               for x, y, text, fg, bg in frame]

def simulcast(*animations):
    for frames in zip(*animations):
        yield [tup for frame in frames for tup in frame]
