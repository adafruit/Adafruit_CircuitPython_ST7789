# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio, set display brightness and draw a solid green
background, a smaller purple rectangle, and some yellow text. The test also has the option of
rotating the screen content.
"""

import board
import displayio
import terminalio
from adafruit_display_text import label
from fourwire import FourWire

from adafruit_st7789 import ST7789

# set the display rotation
rotation = 90
if rotation not in {0, 90, 180, 270}:
    raise ValueError("The value of rotation must be one of: 0, 90, 180, 270")

# Display settings depending on the selected rotation
# first value default setting for 1.69" with 0° and 180° rotation
# second value default setting for 1.69" with 90° and 270° rotation
width = 240 if rotation in {0, 180} else 280
height = 280 if rotation in {0, 180} else 240
color_bitmap_x = 240 if rotation in {0, 180} else 280
color_bitmap_y = 280 if rotation in {0, 180} else 240
inner_bitmap_x = 200 if rotation in {0, 180} else 240
inner_bitmap_y = 240 if rotation in {0, 180} else 200
scale = 2 if rotation in {0, 180} else 3
x = 50 if rotation in {0, 180} else 37
y = 140 if rotation in {0, 180} else 120

# Release any resources currently in use for the displays
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D20
tft_dc = board.D21
backlight = board.D6
display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D5)
display = ST7789(
    display_bus,
    width=width,
    height=height,
    colstart=0,
    rowstart=20,
    rotation=rotation,
    backlight_pin=backlight,
    bgr=True,
    invert=True,
)

# set the backlight
# minimum value 0.001 (0.000 would be off), maximum value 1.000
display.brightness = 0.5

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Draw background rectangle
color_bitmap = displayio.Bitmap(color_bitmap_x, color_bitmap_y, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FF00  # Bright Green
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(inner_bitmap_x, inner_bitmap_y, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xAA0088  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
text_group = displayio.Group(scale=scale, x=x, y=y)
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass
