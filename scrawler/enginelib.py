"""Framework for running an animation."""

import os
from collections import namedtuple
from time import sleep, time

from .colorlib import black, white

GOTO_ORIGIN = '\033[H'

Term = namedtuple('Term', 'Hz width height center_x center_y')

def run(animation):
    term = Term(60, 80, 24, 5, 5)
    period = 1.0 / term.Hz
    t0 = time()
    for frame in animation(term):
        canvas = render(term, frame)
        ansi = ''.join(serialize(canvas))
        os.write(1, ansi.encode('utf-8'))
        tnext = t0 + period
        tnow = time()
        if tnow < tnext:
            sleep(tnext - tnow)
        t0 = time()

def render(term, frame):
    slots = term.height * term.width - 1
    characters = [' '] * slots
    foreground = [black] * slots
    background = [white] * slots

    for x, y, text, fg, bg in frame:
        length = len(text)
        i = term.width * y + x
        j = i + length
        characters[i:j] = text
        foreground[i:j] = [fg] * length
        background[i:j] = [bg] * length

    return characters, foreground, background

def serialize(canvas):
    characters, foreground, background = canvas
    yield GOTO_ORIGIN
    for character, fg, bg in zip(characters, foreground, background):
        yield character
