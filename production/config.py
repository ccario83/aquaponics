import board

## PIN ASSIGNMENT ##
#------------------#
ETAPE_PIN    = board.A1
AQUARIUM_PIN = board.D10
FILL_PIN     = board.D11
DRAIN_PIN    = board.D5  # Pin 5 has 5V output, which is required for the USB relay
ETAPE_BUFFER = 100


## CALIBRATING THE E-TAPE ##
#--------------------------#
HIGH_READING   = 49725 # raw reading
LOW_READING    = 48444 # raw reading
HIGH_MARK      = 2.5   # in
LOW_MARK       = 0.8   # in


## DEPTH CHECK PARAMETERS ##
#--------------------------#
DEPTH_CHECK_TIME  = 20  # seconds
MAX_PREFILL_DEPTH = 4.0 # inches


## FILLING PARAMETERS ##
#----------------------#
# The amount of time to fill the aquaponics bed
FILL_TIME = 20 # seconds


## DRAINING PARAMETERS ##
#-----------------------#
# The amount of time to wait for draining to complete (900s = 15 minutes)
DRAIN_TIME = 420 # seconds


## WAITING PARAMETERS ##
#----------------------#
# How long to wait between each cycle (21,600s = every 6 hours)
TOTAL_TIME = 21600
WAIT_TIME  = TOTAL_TIME-(DEPTH_CHECK_TIME+FILL_TIME+DRAIN_TIME) # seconds


## DEBUG VALUES##
#---------------#
#DEPTH_CHECK_TIME  = 60  # seconds
#MAX_PREFILL_DEPTH = 4.0 # inches
#FILL_TIME = 10 # seconds
#DRAIN_TIME = 10 # seconds
#TOTAL_TIME = 100
#WAIT_TIME  = TOTAL_TIME-(DEPTH_CHECK_TIME+FILL_TIME+DRAIN_TIME) # seconds


assert(WAIT_TIME>0)
assert(TOTAL_TIME>=(DEPTH_CHECK_TIME+FILL_TIME+DRAIN_TIME))