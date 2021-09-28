# This repository contains different programs for LewanSoul smart servos (LX-16A)

## Preconditions
- Python 3
- pyserial package (install it by command: pip install pyserial)
- Set the correct SERIAL_PORT value in lx_setup.py

The shared code (lewansoul_lx16a.py) reused from:<br/>
https://github.com/maximkulkin/lewansoul-lx16a

# src/lx_setup.py
This is a configuration utility for smart servos that can be run on Windows/Linux/MacOS

## Examples of usage:

To check the status of single servo connected to controller:<br/>
**python lx_setup.py**

To scan all servos connected to controller and print their id-s:<br/>
**python lx_setup.py scan**

To change servo id from 2 to 10:<br/>
**python lx_setup.py assign 2 10**

To move servo with id 3 to position 500 (the servo range is from 0 to 1000):<br/>
**python lx_setup.py set_pos 3 500**

# src/controller.py
This is an utility to control the robot arm:
https://cults3d.com/en/3d-model/various/6dof-robot-arm-v2

## Examples of usage:

To record the sequence:<br/>
**python controller.py record**

To play the recording:<br/>
**python controller.py play**
