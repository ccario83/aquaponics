# aquaponics

This repo contains control software for an Adafruit Feather RP2040, which is used to automate an aquaponics system. The goal of this projects is to use nitrate rich water from a fish aquarium to fertilize plants in a tank above the aquarium, and then to return the purified water back to the fish tank.

Here's the setup:

![](setup.png)



The RP2040 cycles the water in a simple fashion: 

1. Check the water level of the plant aquarium bed using an [eTape](https://www.adafruit.com/product/3828?gad_source=1)
2. If the level is sufficiently low, trigger a [relay](relay.png) to pump water into the plant tank until the eTape registers it as full (or a cutoff time is reached)
3. After 15 minutes of irrigation, trigger a second relay to pump the water back into the fish tank
4. Wait a predetermined amount of time (~6 hours) and repeat

