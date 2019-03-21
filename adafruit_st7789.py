# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_st7789`
====================================================

Displayio driver for ST7789 based displays.

* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* Adafruit 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD:
  https://www.adafruit.com/product/3787

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import displayio

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ST7789.git"

_INIT_SEQUENCE = (
    b"\x01\x80\x32" # _SWRESET and Delay 50ms
    b"\x11\x80\xFF" # _SLPOUT
    b"\x3A\x81\x05\x0A" # _COLMOD
    b"\xB1\x83\x00\x06\x03\x0A" # _FRMCTR1
    b"\x36\x01\x08" # _MADCTL
    b"\xB6\x02\x15\x02" # _DISSET5
    #1 clk cycle nonoverlap, 2 cycle gate, rise, 3 cycle osc equalize, Fix on VTL
    b"\xB4\x01\x00" # _INVCTR line inversion
    b"\xC0\x82\x02\x70\x0A" # _PWCTR1 GVDD = 4.7V, 1.0uA, 10 ms delay
    b"\xC1\x01\x05" # _PWCTR2 VGH = 14.7V, VGL = -7.35V
    b"\xC2\x02\x01\x02" # _PWCTR3 Opamp current small, Boost frequency
    b"\xC5\x82\x3C\x38\x0A" # _VMCTR1
    b"\xFC\x02\x11\x15" # _PWCTR6
    b"\xE0\x10\x09\x16\x09\x20\x21\x1B\x13\x19\x17\x15\x1E\x2B\x04\x05\x02\x0E" # _GMCTRP1 Gamma
    b"\xE1\x90\x0B\x14\x08\x1E\x22\x1D\x18\x1E\x1B\x1A\x24\x2B\x06\x06\x02\x0F\x0A" # _GMCTRN1
    b"\x2a\x00\x02\x00\x81" # _CASET
    b"\x2b\x00\x02\x00\x81" # _RASET
    b"\x13\x80\x0a" # _NORON
    b"\x29\x80\xFF" # _DISPON
)

# pylint: disable=too-few-public-methods
class ST7789(displayio.Display):
    """ST7789 driver"""
    def __init__(self, bus, *, width, height):
        super().__init__(bus, _INIT_SEQUENCE, width=width, height=height, colstart=2, rowstart=1)
