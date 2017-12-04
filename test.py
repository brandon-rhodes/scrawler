import scrawler.api as sc

def simple_animation(term):
    y = term.center_y
    duration = term.Hz
    line1 = sc.center_text(term, y-1, 'Beautiful')
    line2 = sc.center_text(term, y, 'is better')
    line3 = sc.center_text(term, y+1, 'than ugly')
    yield from sc.fade_in(line1, duration)
    yield from sc.simulcast(line1, sc.fade_in(line2, duration))
    yield from sc.simulcast(line1, line2, sc.fade_in(line3, duration))

sc.run(simple_animation)
