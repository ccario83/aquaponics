import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Display setup
def setup_display():
    displayio.release_displays()
    i2c = board.I2C()
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
    splash = displayio.Group()
    progress_bar = displayio.Bitmap(display.width, display.height, 2)
    palette = displayio.Palette(2)
    palette[0] = 0x000000
    palette[1] = 0xffffff
    tile_grid = displayio.TileGrid(progress_bar, pixel_shader=palette)
    splash.append(tile_grid)
    text = "Starting ... "
    #main_status_disp = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
    main_status_disp = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=1, y=10)
    sub_status_disp  = label.Label(terminalio.FONT, text='', color=0xFFFF00, x=1, y=25)
    splash.append(main_status_disp)
    splash.append(sub_status_disp)
    display.show(splash)
    return (display, progress_bar, main_status_disp, sub_status_disp)