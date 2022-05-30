import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

#SERIESRESISTOR = 560
HIGH_READING   = 32000
LOW_READING    = 41600
HIGH_MARK      = 4.6 # in
LOW_MARK       = 0.5 # in
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


def fill_aquaponics(max_time=10, max_depth=5):
    start = time.time()
    elapsed = 0
    depth   = 0
    while elapsed <= max_time and depth <= max_depth:
        depth   = read_depth()
        print(f"Time: {elapsed}s, Depth: {depth:.2f}in");
        time.sleep(.2)
        elapsed = time.time() - start


print("[TEST]")

print("Testing A01, e-tape")
etape = AnalogIn(board.A1)
print(f"[E-tape reading: {etape.value}: {read_depth()} in.]");
time.sleep(0.1)

print("Testing D10, aquarium electronics")
aquarium_enable = DigitalInOut(board.D10)
aquarium_enable.direction = Direction.OUTPUT
aquarium_enable.value = False
time.sleep(1.0)
aquarium_enable.value = True
time.sleep(1.0)

print("Testing D11, aquaponic filling")
fill_pause = DigitalInOut(board.D11)
fill_pause.direction  = Direction.OUTPUT
fill_pause.value = False
time.sleep(1.0)
fill_pause.value = True
time.sleep(1.0)

print("Testing D12, aquaponic drain")
drain_pause = DigitalInOut(board.D12)
drain_pause.direction  = Direction.OUTPUT
drain_pause.value = False
time.sleep(1.0)
drain_pause.value = True

time.sleep(3.0)
print("[Starting]")
while True:
    print("Disabling aquarium electronics...")
    # Disable the aquarium heater, water pump, and air pump
    aquarium_enable.value = False
    time.sleep(1.0)

    print("Filling the aquaponic tank...")
    fill_pause.value = False
    fill_aquaponics(max_depth=100)
    # While low water level or time not reached
    # Start the aquaponic fill pump
    # level = read_water_level()
    # while level < 6.0
    #     fill_pause.value = False
    #     level = read_water_level()
    #     time.sleep(5)
    # Disable the aquaponic fill pump
    fill_pause.value = True
    time.sleep(0.25)
    # Wait for 15 minutes
    print("Irrigation soak...")
    time.sleep(5.0)
    
    # Start the aquaponic drain
    print("Draining the aquaponic tank...")
    drain_pause.value = False
    time.sleep(5.0)
    # level = read_water_level()
    # while level >= 1.0
    #     drain_pause.value = True
    #     level = read_water_level()
    #     time.sleep(5)
    # Disable the aquaponic fill pump
    # fill_pause.value = True
    # time.sleep(1)
    #print("Stopping drain pump...")
    drain_pause.value = True
    #time.sleep(0.55)
    print("Enabling aquarium electronics...")
    aquarium_enable.value  = True
    time.sleep(5.0)