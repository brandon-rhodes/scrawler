"""ASCII art animation framework.

As made famous in my 2017 North Bay Python keynote talk, this library
lets you create animations for your terminal screen::

    import scrawler.api as sc

    def simple_animation(frame):
        y = frame.center_y
        duration = frame.Hz
        line1 = sc.center_text(y-1, 'Beautiful')
        line2 = sc.center_text(y, 'is better')
        line3 = sc.center_text(y+2, 'than ugly')
        yield from sc.fade_in(line1, duration)
        yield from sc.simulcast(line1, fade_in(line2, duration))
        yield from sc.simulcast(line1, line2, fade_in(line3, duration))

    sc.run(simple_animation)

"""
