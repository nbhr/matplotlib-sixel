Matplotlib-sixel backend
========================

A matplotlib backend which outputs sixel graphics onto the terminal.
The code is inspired by the ipython-notebook matplotlib backend.

Dependencies
------------

* terminal with Sixel support configured.
* imagemagick (for converting the graphics)
* matplotlib

Installation
-------------

    pip install matplotlib-sixel

Usage
-----


    import matplotlib
    import numpy

    matplotlib.use('module://matplotlib-sixel')
    from pylab import *
    plt.plot(sin(arange(100) / 10))
    show()
