import time
from config import *
from util import *
from display import *

(display, progress_bar, main_status_disp, sub_status_disp) = setup_display()

#test_electronics(main_status_disp, sub_status_disp)

# Set global color
color = 1
next_color_time = display.width
# Set timer info
start = time.time()
cycle_start_time = None
# Set status and display lines
error  = False
status = 'Waiting'
line1  = ''
line2  = ''
# Set initial relay states
aquarium.value     = True
fill_disable.value = True
drain.value        = False
# Set variables for depth calculations
depths = [0.5]*ROLLING_NUM
depths_avg = 0
depth_num = 0
while True:
    #print(f"STATUS: {status}  ERROR: {error}  LINE1: {line1}  LINE2: {line2}")
    # Find the current elapsed time and update the progress bar
    elapsed = time.time() - start

    # Update the display
    progress_bar[elapsed%display.width, 0] = color
    if elapsed >= next_color_time:
        color = abs(color - 1)
        next_color_time = elapsed + display.width
    if main_status_disp.text != line1:
        main_status_disp.text = line1
    if main_status_disp.text != line2:
        sub_status_disp.text  = line2
    
    # Code to run if in a cycle
    if error:
        status = None
        #start  = time.time()
    elif elapsed>=TIME_BETWEEN_CYCLES:
        # At the very beginning of the cycle, switch to filling
        if not cycle_start_time:
            status = 'Filling'
            cycle_start_time = time.time()
            # Update relays
            aquarium.value     = False
            fill_disable.value = False
            drain.value        = False
        
        # Update the cycle time (s)
        cycle_time = time.time() - cycle_start_time
        # While filling
        if status is 'Filling':
            # Fill the aquaponic bed
            if cycle_time <= MAX_FILL_TIME and depths_avg <= STOP_FILL_DEPTH:
                # Get the current depth and calculate a (more) stable rolling average
                (depth,_) = read_depth()
                depths[(depth_num%ROLLING_NUM)] = depth
                depths_avg = float(sum(depths)/ROLLING_NUM)
                line1 = f"Cycling {cycle_time:4,d} | {MAX_FILL_TIME:4,d} s"
                # Update the display
                if depth_num>=ROLLING_NUM:
                    #line2=f"{_}"
                    line2 = f" Filling  @  {depths_avg:2.1f}in"
                else:
                    #line2=f"{_}"
                    line2 = f" Filling  ~  {depths_avg:2.1f}in"
                depth_num+=1
            # End the filling stage and begin draining
            else:
                # Check that the tank was filled, assuming MAX_FILL_TIME was reached first
                if depths_avg <= MIN_FILL_DEPTH:
                    error  = True
                    line1  = 'Error!'
                    line2  = 'Failed to fill!'
                    aquarium.value     = False
                    fill_disable.value = True
                    drain.value        = False
                else:
                    # Change the status to 'Draining' and continue
                    status = 'Draining'
                    # Update relays
                    aquarium.value     = False
                    fill_disable.value = True
                    drain.value        = True
                    # Update timers and depth calculators
                    drain_start_time = time.time()
                    #depths = [3.5]*ROLLING_NUM
                    #depth_num = 0

        elif status is 'Draining':
            drain_duration = time.time() - drain_start_time
            if drain_duration <= MAX_DRAIN_TIME and depths_avg >= STOP_DRAIN_DEPTH:
                (depth,_) = read_depth()
                depths[(depth_num%ROLLING_NUM)] = depth
                depths_avg = float(sum(depths)/ROLLING_NUM)
                line1 = f"Cycling {drain_duration:4,d} | {MAX_DRAIN_TIME:4,d} s"
                if depth_num>=ROLLING_NUM:
                    #line2=f"{_}"
                    line2 = f" Draining @ {depths_avg:2.1f}in"
                else:
                    #line2=f"{_}"
                    line2 = f" Draining ~ {depths_avg:2.1f}in"
                depth_num+=1

            # End the draining stage and reset all variables to begin waiting again
            else:
                # Check that the tank was drained, assuming MAX_DRAIN_TIME was reached first
                if depths_avg >= MAX_DRAIN_DEPTH:
                    error  = True
                    line1  = 'Error!'
                    line2  = 'Failed to drain!'
                    aquarium.value     = False
                    fill_disable.value = True
                    drain.value        = False
                else:
                    # Change the status to 'Draining' and continue
                    status = 'Waiting'
                    line1 = f""
                    line2 = f""
                    # Update relays
                    aquarium.value     = True
                    fill_disable.value = True
                    drain.value        = False
                    # Reset cycle timers and progress bar
                    color = 1
                    next_color_time = display.width
                    start = time.time()
                    cycle_start_time = None
                    cycle_time = None
                    drain_start_time = None
                    # Reset depth calculation variables
                    #depths = [0.5]*ROLLING_NUM
                    depths_avg= 0
                    depth_num = 0
    # Waiting between cycles
    else:
        time_left = TIME_BETWEEN_CYCLES-elapsed
        line1 = f"Waiting {time_left:5,d} s"

