import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

import displayio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
splash = displayio.Group()
display.show(splash)


#SERIESRESISTOR = 560
HIGH_READING   = 46800
LOW_READING    = 50500
HIGH_MARK      = 4.6 # in
LOW_MARK       = 0.5 # in



def fill_aquaponics(max_time=20, max_depth=5):
    start = time.time()
    fill_pause.value=False
    
    elapsed = 0
    depth   = 0
    while elapsed <= max_time and depth <= max_depth:
        depth   = read_depth()
        print(f"Time: {elapsed}s, Depth: {depth:.2f}in");
        time.sleep(.2)
        elapsed = time.time() - start
    fill_pause.value=True


#def drain_aquaponics(max_time=600, min_depth=1.0):


def test_electronics():
    print("Lights off")
    fill_pause.value = True
    aquarium_enable.value  = True
    time.sleep(3.0)

    print("Fill relay test")
    print("FILL ON (light on)")
    fill_pause.value = False
    time.sleep(3.0)
    print("FILL OFF (light off)")
    fill_pause.value = True
    time.sleep(3.0)

    print("Aquarium relay test")
    print("AQUARIUM OFF (light on)")
    aquarium_enable.value = False
    time.sleep(3.0)
    print("AQUARIUM ON (light off)")
    aquarium_enable.value = True
    time.sleep(3.0)

    time.sleep(5)

#test_electronics()

start = time.time()
while True:
    elapsed = time.time() - start
    print(f"Turning aquarium electronics off...")
    aquarium_enable.value = False
    time.sleep(1)
    print(f"Filling...")
    fill_aquaponics()
    print(f"Filled!")
    #Wait 60 seconds
    time.sleep(1)
    print(f"Turning aquarium electronics on...")
    aquarium_enable.value = True

    #21,600 (6 hours)
    time.sleep(15)