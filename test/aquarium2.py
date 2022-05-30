import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

#SERIESRESISTOR = 560
HIGH_READING   = 46800
LOW_READING    = 50500
HIGH_MARK      = 4.6 # in
LOW_MARK       = 0.5 # in

etape = AnalogIn(board.A2)

fill_pause = DigitalInOut(board.D12)
fill_pause.direction  = Direction.OUTPUT
fill_pause.value = True

aquaponics_drain = DigitalInOut(board.D10)
aquaponics_drain.direction  = Direction.OUTPUT
aquaponics_drain.value = True

aquarium_enable = DigitalInOut(board.D11)
aquarium_enable.direction = Direction.OUTPUT
aquarium_enable.value = True

def read_depth(hr=HIGH_READING, hm=HIGH_MARK, lr=LOW_READING, lm=LOW_MARK):
    # Find the linear relationship
    # y= mx + b
    # m = (y2-y1)/(x2-x1)
    # b = y - mx
    m = (lm - hm)/(lr - hr)
    b = hm - (m * hr)
    
    # Read the etape
    reading = etape.value
    if reading is not 0:
        if reading < hm:
            reading = 0
        else:
            reading = (m * reading) + b;
        if reading < 0:
            reading = 0
    
    return reading


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

while True:
    
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