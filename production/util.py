import time
from config import *
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

etape = AnalogIn(ETAPE_PIN)

fill_disable = DigitalInOut(FILL_PIN)
fill_disable.direction = Direction.OUTPUT
fill_disable.value = True

drain = DigitalInOut(DRAIN_PIN)
drain.direction = Direction.OUTPUT
drain.value = True

aquarium = DigitalInOut(AQUARIUM_PIN)
aquarium.direction = Direction.OUTPUT
aquarium.value = True


depths    = None
depth_num = None
def check_depth():
    global depths
    global depth_num
    # Initialize
    if depths == None:
        depths    = [.5]*ETAPE_BUFFER
        depth_num = 0

    # Read the depth and update the rolling average
    (depth, _) = read_depth()

    # Start recycling the vector if it gets too large
    if depth_num>=ETAPE_BUFFER:
        depth_num = 0
    depths[depth_num] = depth

    depth_num += 1
    # Return the average reading
    depths_avg = float(sum(depths)/len(depths))
    return depths_avg


def set_fill():
    aquarium.value = False
    fill_disable.value = False
    drain.value = False
    return


def set_drain():
    aquarium.value = False
    fill_disable.value = True
    drain.value = True
    return


# Only change the state if needed
def set_wait():
    aquarium.value = True
    fill_disable.value = True
    drain.value = False
    return


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
    
    return (reading, etape.value)


def test_electronics(main_disp, sub_disp):
    # Test the relays
    main_disp.text = f"Light test..."
    sub_disp.text = f"AQ * | FL - | DR -"
    aquarium.value = False
    fill_disable.value = True
    drain_disable.value = True
    time.sleep(3.0)

    main_disp.text = f"Light test..."
    sub_disp.text = f"AQ - | fill * | DR -"
    aquarium.value = True
    fill_disable.value = False
    drain_disable.value = True
    time.sleep(3.0)

    main_disp.text = f"Light test..."
    sub_disp.text = f"AQ - | fill - | DR *"
    aquarium.value = True
    fill_disable.value = True
    drain_disable.value = False
    time.sleep(3.0)

    # Now test the logic
    main_disp.text = f"Logic test (Waiting)..."
    sub_disp.text = f"AQ - | fill - | DR -"
    aquarium.value = True
    fill_disable.value = True
    drain_disable.value = True
    time.sleep(10.0)

    main_disp.text = f"Logic test (Filling)..."
    sub_disp.text = f"AQ * | fill * | DR -"
    aquarium.value = False
    fill_disable.value = False
    drain_disable.value = True
    time.sleep(10.0)

    main_disp.text = f"Logic test (Draining)..."
    sub_disp.text = f"AQ * | fill - | DR *"
    aquarium.value = False
    fill_disable.value = True
    drain_disable.value = False
    time.sleep(5.0)

    main_disp.text = f""
    sub_disp.text = f""