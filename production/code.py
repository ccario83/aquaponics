import time
from config import *
from util import *
from display import *


#test_electronics(main_status_disp, sub_status_disp)

# Initialize display
setup_display()

# Initialize the cycle time
elapsed          = 0
cycle_start_time = time.time()

# Set the initial wait stage parameters
stage            = 'Waiting'
stage_start_time = cycle_start_time
stage_end_time   = WAIT_TIME
stage_time       = 0
set_wait()


# While no error
while True:
    # Update the cycle time and display
    stage_time = time.time() - stage_start_time
    time_left  = stage_end_time - stage_time

    # The waiting stage
    if stage == 'Waiting':
        line1 = f"Waiting {time_left:5,d} s"
        line2 = f""
        # When the wait's up, begin the water cycle
        if stage_time >= stage_end_time:
            stage            = 'Depth Check'
            stage_start_time = time.time()
            stage_end_time   = DEPTH_CHECK_TIME
            stage_time       = 0


    # The depth check stage
    elif stage == 'Depth Check':
        depth = check_depth()
        line1 = f"Check {stage_time:4,d} | {stage_end_time:4,d} s"
        line2 = f"Depth @ {depth:2.1f} in"

        # When done
        if stage_time >= stage_end_time:
            # Make sure the tank can be filled, or break while in error
            if depth >= MAX_PREFILL_DEPTH:
                line1  = 'Error!'
                line2 = f"Depth @ {depth:2.1f} in"
                percent_progress = elapsed/TOTAL_TIME
                update_display(percent_progress, line1, line2)
                set_wait()
                break
            # Move on to the next stage
            else:
                stage            = 'Fill'
                stage_start_time = time.time()
                stage_end_time   = FILL_TIME
                stage_time       = 0
                set_fill()


    # The filling stage
    elif stage == 'Fill':
        depth = check_depth()
        line1 = f"Fill {stage_time:4,d} | {stage_end_time:4,d} s"
        line2 = f"Depth @ {depth:2.1f} in"

        # When done
        if stage_time >= stage_end_time:
            stage            = 'Drain'
            stage_start_time = time.time()
            stage_end_time   = DRAIN_TIME
            stage_time       = 0
            set_drain()


    # The draining stage
    elif stage == 'Drain':
        depth = check_depth()
        line1 = f"Drain {stage_time:4,d} | {stage_end_time:4,d} s"
        line2 = f"Depth @ {depth:2.1f} in"

        # When done
        if stage_time >= stage_end_time:
            stage            = 'Waiting'
            stage_start_time = time.time()
            stage_end_time   = WAIT_TIME
            stage_time       = 0
            set_wait()
            # Reset cycle timers and progress bar
            cycle_start_time= time.time()

    # Not a valid stage!
    else:
        line1 = f"Invalid stage!"
        set_wait()
        break

    # Find the current elapsed time and update the progress bar
    elapsed = time.time() - cycle_start_time

    # Update the display
    percent_progress = elapsed/TOTAL_TIME
    update_display(percent_progress, line1, line2)
    #print(f"STAGE: {stage} LINE1: {line1}  LINE2: {line2}")
