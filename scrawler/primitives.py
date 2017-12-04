"""Visual elements."""

from itertools import repeat
from .colorlib import black

def center_text(term, y, text, fg=black, bg=None):
    x = (term.width - len(text)) // 2
    yield from repeat([(x, y, text, fg, bg)])
