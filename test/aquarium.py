import time
import board
from digitalio import DigitalInOut, Direction

print("[TEST]")

print("Testing D5")
aquarium_enable = DigitalInOut(board.D5)
aquarium_enable.direction = Direction.OUTPUT
aquarium_enable.value = False
time.sleep(1.0)
aquarium_enable.value = True
time.sleep(1.0)

print("Testing D9")
fill_pause = DigitalInOut(board.D9)
fill_pause.direction  = Direction.OUTPUT
fill_pause.value = False
time.sleep(1.0)
fill_pause.value = True
time.sleep(1.0)

print("Testing D11")
drain_pause = DigitalInOut(board.D11)
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
    time.sleep(5.0)
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