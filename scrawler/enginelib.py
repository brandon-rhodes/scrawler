"""Framework for running an animation."""

import os
from collections import namedtuple
from shutil import get_terminal_size

from time import sleep, time

from .colorlib import black, white, apply_alpha

HIDE_CURSOR = b'\033[?25l'
SHOW_CURSOR = b'\033[?12l\033[?25h'
GOTO_ORIGIN = '\033[H'
FG = '\033[38;2;{};{};{}m'
BG = '\033[48;2;{};{};{}m'

Term = namedtuple('Term', 'Hz width height center_x center_y')

def run(animation):
    os.write(1, HIDE_CURSOR)
    try:
        _run(animation)
    finally:
        os.write(1, SHOW_CURSOR)

def _run(animation):
    width, height = get_terminal_size()
    term = Term(60, width, height, width // 2, height // 2)
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
    background = [white[:3]] * slots
    foreground = [black[:3]] * slots

    for x, y, text, fg, bg in frame:
        length = len(text)
        i = term.width * y + x
        j = i + length
        characters[i:j] = text
        if bg is not None:
            background[i:j] = [apply_alpha(bg, obg) for obg in background[i:j]]
        if fg is not None:
            foreground[i:j] = [apply_alpha(fg, obg) for obg in background[i:j]]

    return characters, foreground, background

def serialize(canvas):
    characters, foreground, background = canvas
    yield GOTO_ORIGIN
    ofg = obg = None
    for character, fg, bg in zip(characters, foreground, background):
        if (fg is not None) and fg != ofg:
            r, g, b = fg
            yield FG.format(int(255.0 * r),
                            int(255.0 * g),
                            int(255.0 * b))
            ofg = fg
        if (bg is not None) and bg != obg:
            r, g, b = bg
            yield BG.format(int(255.0 * r),
                            int(255.0 * g),
                            int(255.0 * b))
            obg = bg
        yield character
