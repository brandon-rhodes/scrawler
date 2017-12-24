
import unittest
from scrawler.effects import fade_in

class Tests(unittest.TestCase):

    def test_fade_in(self):
        frames = [(3, 4, 'Tx', (0.4, 0.5, 0.6, 0.75), (0.6, 0.8, 1.0, 0.375))]
        frames = list(fade_in([frames] * 4, 3))
        self.assertEqual(frames, [
            [(3, 4, 'Tx', (0.4, 0.5, 0.6, 0.25), (0.6, 0.8, 1.0, 0.125))],
            [(3, 4, 'Tx', (0.4, 0.5, 0.6, 0.5), (0.6, 0.8, 1.0, 0.250))],
            [(3, 4, 'Tx', (0.4, 0.5, 0.6, 0.75), (0.6, 0.8, 1.0, 0.375))],
        ])
