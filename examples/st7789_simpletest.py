"""
This test will initialize the display using displayio
and draw a solid red background
"""

import board
import displayio
from adafruit_st7789 import ST7789

spi = board.SPI()
while not spi.try_lock():
    pass
spi.configure(baudrate=24000000) # Configure SPI for 24MHz
spi.unlock()
tft_cs = board.D5
tft_dc = board.D6

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D9)

display = ST7789(display_bus, width=240, height=240, rowstart=80)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

try:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   position=(0, 0))
except TypeError:
    bg_sprite = displayio.TileGrid(color_bitmap,
                                   pixel_shader=color_palette,
                                   x=0, y=0)
splash.append(bg_sprite)

while True:
    pass
