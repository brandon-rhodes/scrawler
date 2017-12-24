
# Scrawler

An ASCII art animation library
that I am assembling from the ideas
in my 2017 opening keynote at the North Bay Python conference:

https://www.youtube.com/watch?v=rrMnmLyYjU8

Scrawler is small, but you can try it out with:

    git clone git@github.com:brandon-rhodes/scrawler.git
    cd scrawler
    python3 -m scrawler.examples.zen

Note that some terminals are better for animation than others.
The venerable `xterm` is quite poor,
and animations run inside of it will flicker incessantly.
But I have not observed any flickering
when running my animations in a terminal launched with:

    xfce4-terminal --hide-menubar

You can run Scrawler’s tests with:

    python3 -m unittest discover
