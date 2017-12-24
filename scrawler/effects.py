"""Visual effects."""

def fade_in(animation, duration):
    """Make an `animation` fade in over `duration` frames.

    Consume the first `duration` frames of `animation`, yielding them
    with their transparency reduced so the foreground and background
    colors fade in from transparent to opaque.

    """
    if duration > 2:
        alphas = [i / duration for i in range(1, duration + 1)]
    elif duration == 2:
        alphas = 0.5, 1.0
    else:
        alphas = 1.0,

    for alpha, frame in zip(alphas, animation):
        yield [(x, y, text, (fg[0], fg[1], fg[2], fg[3] * alpha),
                bg if bg is None else (bg[0], bg[1], bg[2], bg[3] * alpha))
               for x, y, text, fg, bg in frame]

def simulcast(*animations):
    """Yield frames made by combining the frames from several animations.

    Like `zip()`, this routine stops consuming frames from the
    animations as soon as any one of them reaches its conclusion.

    """
    for frames in zip(*animations):
        yield [tup for frame in frames for tup in frame]
