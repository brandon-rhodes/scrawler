from random import choice, randrange
import scrawler.api as sc

def zen(term):
    y = term.center_y
    duration = term.Hz
    line1 = sc.center_text(term, y-2, 'Beautiful')
    line2 = sc.center_text(term, y-1, 'is better')
    line3 = sc.center_text(term, y, 'than ugly')
    yield from sc.fade_in(line1, duration)
    yield from sc.simulcast(line1, sc.fade_in(line2, duration))
    yield from sc.simulcast(line1, line2, sc.fade_in(line3, duration))
    final_frame = next(line1) + next(line2) + next(line3)
    while True:
        yield final_frame

def cointoss():
    return choice((0, 1))

def boxes_of_color(term, color):
    r, g, b = color
    c = r, g, b, 0.5
    width = 9
    height = 5
    row = ' ' * width

    # So all the boxes don't enter and exit at the same moments.
    delay_between_runs = range(choice((2,3,5,7,11,13)))

    while True:
        for i in delay_between_runs:
            yield []
        if cointoss():
            ax = range(-width, term.width + width)
            if cointoss():
                ax = ax[::-1]
            y = randrange(0, term.height - height)
            for x in ax:
                yield [(x, y + i, row, sc.black, c) for i in range(height)]
        else:
            ay = range(-height, term.height + height)
            if cointoss():
                ay = ay[::-1]
            x = randrange(0, term.width - width)
            for y in ay:
                yield [(x, y + i, row, sc.black, c) for i in range(height)]

def slow(animation, factor=4):
    r = range(factor)
    for frame in animation:
        for i in r:
            yield frame

def clip(term, animation):
    for frame in animation:
        yield list(clip_frame(term, frame))

def clip_frame(term, frame):
    for x, y, text, fg, bg in frame:
        if 0 <= y < term.height:
            if x < 0:
                text = text[-x:]
                x = 0
            excess = x + len(text) - term.width
            if excess > 0:
                text = text[:-excess]
            if text:
                yield x, y, text, fg, bg

def simple_animation(term):
    yield from clip(term, sc.simulcast(
        slow(boxes_of_color(term, (1, 0, 0)), randrange(3, 6)),
        slow(boxes_of_color(term, (1, 1, 0)), randrange(3, 6)),
        slow(boxes_of_color(term, (0, 1, 0)), randrange(3, 6)),
        slow(boxes_of_color(term, (0, 1, 1)), randrange(3, 6)),
        slow(boxes_of_color(term, (0, 0, 1)), randrange(3, 6)),
        zen(term),
    ))


if __name__ == '__main__':
    sc.run(simple_animation)
