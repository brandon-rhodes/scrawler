"""Framework for running an animation."""

from collections import namedtuple

Term = namedtuple('Term', 'Hz width height center_x center_y')

def run(animation):
    term = Term(60, 10, 10, 5, 5)
    for frame in animation(term):
        print(frame)
