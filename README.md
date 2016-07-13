# Python Module for Standa 8SMC1-USBhF

Python module for controlling Standa 8SMC1-USBhF Motor Controller connected to a Windows PC over USB. Developed by Sam Hutchings whilst working on a student Summer Research Project in the Physics department at the [University of Exeter](http://emps.exeter.ac.uk/physics-astronomy/).

## Dependencies
* Windows Only - Tested on Windows 7 and 10
* MicroSMC - included in downloads available from the product page on Standa's website [here](http://www.standa.lt/products/catalog/motorised_positioners?item=175).

## Binaries
The ```binaries``` folder contains two executables:

* ```ListConnectedStandaDevices.exe``` - Prints the currently connected Standa devices connected to the system to the command line, showing the current device ID and the serial number for each device. If the last four characters are entered as the first parameter, the program will return the device id of that controller as its return code, provided the device is connected to the system.

* ```StandaStepperMotorController.exe``` - 
