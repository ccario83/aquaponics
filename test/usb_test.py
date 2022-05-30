import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

aquaponics_drain = DigitalInOut(board.D5)
aquaponics_drain.direction  = Direction.OUTPUT
aquaponics_drain.value = True

while True:
    print("OFF")
    aquaponics_drain.value=False
    time.sleep(3)
    aquaponics_drain.value=True
    print("ON")
    time.sleep(3)
