import time
import board
from analogio import AnalogIn

SERIESRESISTOR = 560

etape = AnalogIn(board.A0)

while True
    reading = etape.value
    reading = (1023 / reading)  - 1;
    reading = SERIESRESISTOR / reading;
    print(f"Sensor resistance: {reading}"); 

    time.sleep(5)