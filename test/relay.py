import time
import board
from digitalio import DigitalInOut, Direction


```
board.A0
board.A1
board.A2
board.A3
board.D0 board.RX
board.D1 board.TX
board.D10
board.D11
board.D12
board.D13 board.LED
board.D24
board.D25
board.D4
board.D5
board.D6
board.D9
board.MISO
board.MOSI
board.NEOPIXEL
board.SCK
board.SCL
board.SDA
```

aqua_outlet = DigitalInOut(board.D5)
aqua_outlet.direction = Direction.OUTPUT

while True:
    aqua_outlet.value = True
    time.sleep(.5)