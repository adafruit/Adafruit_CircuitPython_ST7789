# SPDX-FileCopyrightText: 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_st7789`
====================================================

Displayio driver for ST7789 based displays.

* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* Adafruit 1.3" 240x240 Wide Angle TFT LCD Display with MicroSD - ST7789:
  https://www.adafruit.com/product/4313

* Adafruit 1.54" 240x240 Wide Angle TFT LCD Display with MicroSD - ST7789:
  https://www.adafruit.com/product/3787

* Adafruit 1.14" 240x135 Color TFT Display + MicroSD Card Breakout - ST7789:
  https://www.adafruit.com/product/4383

* Adafruit Mini PiTFT 1.3" - 240x240 TFT Add-on for Raspberry Pi:
  https://www.adafruit.com/product/4484

* Adafruit 1.3" Color TFT Bonnet for Raspberry Pi - 240x240 TFT + Joystick Add-on
  https://www.adafruit.com/product/4506

* Adafruit Mini PiTFT - 135x240 Color TFT Add-on for Raspberry Pi:
  https://www.adafruit.com/product/4393

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

from busdisplay import BusDisplay

try:
    from typing import Any

    from fourwire import FourWire
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_ST7789.git"

_INIT_SEQUENCE = (
    b"\x01\x80\x96"  # _SWRESET and Delay 150ms
    b"\x11\x80\xff"  # _SLPOUT and Delay 500ms
    b"\x3a\x81\x55\x0a"  # _COLMOD and Delay 10ms
    b"\x36\x01\x08"  # _MADCTL
    b"\x13\x80\x0a"  # _NORON and Delay 10ms
    b"\x29\x80\xff"  # _DISPON and Delay 500ms
)


# pylint: disable=too-few-public-methods
class ST7789(BusDisplay):
    """
	  ST7789 driver
	
	  :param FourWire bus: bus that the display is connected to
    :param bool bgr: (Optional) An extra init sequence to append (default=True)
    :param bool invert: (Optional) Invert the colors (default=True)
    """

    def __init__(self, bus: FourWire, *, bgr: bool = True, invert: bool = True, **kwargs: Any):
        init_sequence = _INIT_SEQUENCE
        if bgr:
            init_sequence += b"\x36\x01\xc0"  # _MADCTL Default rotation plus BGR encoding
        else:
            init_sequence += b"\x36\x01\xc8"  # _MADCTL Default rotation plus RGB encoding
        if invert:
            init_sequence += b"\x21\x00"  # _INVON
        super().__init__(bus, init_sequence, **kwargs)