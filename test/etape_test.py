import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

ROLLING_NUM = 200

HIGH_READING   = 49725 # raw reading
LOW_READING    = 48444 # raw reading
HIGH_MARK      = 2.5   # in
LOW_MARK       = 0.8   # in

#HIGH_READING   = 51250
#LOW_READING    = 48455
#HIGH_MARK      = 4.0 # in
#LOW_MARK       = 0.7 # in

etape = AnalogIn(board.A1)

def read_depth(hr=HIGH_READING, hm=HIGH_MARK, lr=LOW_READING, lm=LOW_MARK, reading=None):
    # Find the linear relationship
    # y= mx + b
    # m = (y2-y1)/(x2-x1)
    # b = y - mx
    m = (lm - hm)/(lr - hr)
    b = hm - (m * hr)
    
    # Read the etape
    if reading is None:
        reading = etape.value
    if reading is not 0:
        if reading < hm:
            reading = 0
        else:
            reading = (m * reading) + b;
        if reading < 0:
            reading = 0
    return (etape.value, reading)




elapsed  = 0
depth    = 0
start    = time.time()
rolling  = [0]*ROLLING_NUM
every    = 1
reading_count = 0
while True:
    elapsed = time.time() - start
    (val, depth) = read_depth()
    reading_count+=1
    rolling[(reading_count%ROLLING_NUM)-1]=val
    rolling_avg = int(sum(rolling)/ROLLING_NUM)
    if elapsed%every==0:
        disp = '-'
        eql  = '-'
        if reading_count>=ROLLING_NUM:
            disp = str(rolling_avg)
            eql  = f"{read_depth(reading=rolling_avg)[1]:.1f}"
        print(f"Time: {elapsed}s, Depth: {depth:.1f}in, reading: {val}, {ROLLING_NUM}-value rolling average: {disp}, Depth: {eql}in");