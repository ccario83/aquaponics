import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Static variables
display_width    = None
progress_bar     = None
main_status_disp = None
sub_status_disp  = None

# Display setup
def setup_display():
    global display_width
    global progress_bar
    global main_status_disp
    global sub_status_disp

    i2c = board.I2C()
    # Initialize the display
    displayio.release_displays()
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
    display_width = display.width
    
    # Create a palette of black and white colors
    palette = displayio.Palette(2)
    palette[0] = 0x000000 # Black
    palette[1] = 0xffffff # White

    # Create a progres bar and set a time limit before switching colors
    progress_bar = displayio.Bitmap(display.width, display.height, 2)
    tile_grid = displayio.TileGrid(progress_bar, pixel_shader=palette)

    # Create two status lines
    text = "Starting ... "
    main_status_disp = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=1, y=10)
    sub_status_disp  = label.Label(terminalio.FONT, text='', color=0xFFFF00, x=1, y=25)
    
    # Display
    splash = displayio.Group()
    splash.append(tile_grid)
    splash.append(main_status_disp)
    splash.append(sub_status_disp)
    display.show(splash)
    return


def update_display(percent_progress, line1, line2):
    assert(percent_progress>=0 and percent_progress<=1.0)
    coord = abs(int(percent_progress*display_width)-1)
    progress_bar[coord, 0] = 1
    if main_status_disp.text != line1:
        main_status_disp.text = line1
    if main_status_disp.text != line2:
        sub_status_disp.text  = line2
