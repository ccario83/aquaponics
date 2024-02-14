# Aquaponics Fun

This repo contains control software for an Adafruit Feather RP2040, which is used to automate an aquaponics system. The goal of this project is to use nitrate rich water from a fish aquarium to fertilize plants in a tank above the aquarium, and then to return the purified water back to the fish tank. Its a complete and self contained ecosystem (minus the fish-feeding part)!

Here's the setup:

![](setup.png)



The RP2040 cycles the water in a simple fashion: 

1. Check the water level of the plant aquarium bed using an [eTape](https://www.adafruit.com/product/3828?gad_source=1)
2. If the level is sufficiently low, trigger a [relay](relay.png) to pump water into the plant tank until the eTape registers it as full (or a cutoff time is reached). This step also temporarily turns off the fish tank pump to prevent it from taking up too much air from the sudden decrease in water volume.
4. After 15 minutes of irrigation, trigger a second relay to pump the water back into the fish tank
5. Wait a predetermined amount of time (~6 hours) and repeat

The repo also includes a custom STL file for a 3D printed tank water strainer, which improves water flow such that draining the tank rapidly doesn't cause issues with the fish aquarium pump. 

Some bonus videos/photos
1. [Custom 3D printed strainer](strainer.png)
2. [The system in action](in_action.mp4)
3. [Happy fish!](happy_fish.mp4)
