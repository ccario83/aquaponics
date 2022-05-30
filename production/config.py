import board


## PIN ASSIGNMENT ##
#------------------#
ETAPE_PIN    = board.A1
AQUARIUM_PIN = board.D10
FILL_PIN     = board.D11
DRAIN_PIN    = board.D5  # Pin 5 has 5V output, which is required for the USB relay


## CALIBRATING THE E-TAPE ##
#--------------------------#
HIGH_READING   = 51330 # raw reading
LOW_READING    = 48465 # raw reading
HIGH_MARK      = 4.0   # in
LOW_MARK       = 0.7   # in
ROLLING_NUM    = 100   # How many consecutive raw readings to average for a stable value


## WAITING PARAMETERS ##
#----------------------#
# How long to wait between each cycle (21,600s = every 6 hours)
TIME_BETWEEN_CYCLES = 21600 # seconds


## FILLING PARAMETERS ##
#----------------------#
# The maximum amount of time to fill the aquaponics bed
MAX_FILL_TIME = 20 # seconds
# The depth at which to stop filling if fill time still remains
STOP_FILL_DEPTH = 2.2 # inches
# The minimum depth that must be filled to ensure a working fill pump and no leak
MIN_FILL_DEPTH = 0.9 # inches


## DRAINING PARAMETERS ##
#-----------------------#
# The maximum amount of time to wait for draining to complete (900s = 15 minutes)
MAX_DRAIN_TIME = 420 # seconds
# The depth at which to stop draining if drain time still remains
STOP_DRAIN_DEPTH = 0.8 # inches
# The maximum allowed depth after draining to ensure a working drain pump
MAX_DRAIN_DEPTH = 1.0 # inches


## DEBUG VALUES##
#---------------#
#TIME_BETWEEN_CYCLES = 10
#MAX_FILL_TIME       = 18
#STOP_FILL_DEPTH     = 3.5
#MIN_FILL_DEPTH      = 3.0
#MAX_DRAIN_TIME      = 900
#STOP_DRAIN_DEPTH    = 0.7
#MAX_DRAIN_DEPTH     = 1.0



