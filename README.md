# Python Modules for Standa 8SMC1-USBhF

Python modules for controlling Standa 8SMC1-USBhF Motor Controller connected to a Windows PC over USB. Developed by Sam Hutchings whilst working on a student Summer Research Project in the Physics department at the [University of Exeter](http://emps.exeter.ac.uk/physics-astronomy/).

## Dependencies
* Windows Only - Tested on Windows 7 and 10
* MicroSMC - included in downloads available from the product page on Standa's website [here](http://www.standa.lt/products/catalog/motorised_positioners?item=175). Uses the included *USMCDLL.dll*.

## Binaries
The ```binaries``` folder contains two executables:

### ```ListConnectedStandaDevices.exe```

Prints the currently connected Standa devices connected to the system to the command line, showing the current device ID and the serial number for each device. If the last four characters are entered as the first parameter, the program will return the device id of that controller as its return code, provided the device is connected to the system.

### ```StandaStepperMotorController.exe```

Interfaces with the motor controller. Can be provided with a variety of parameters to execute operations.

#### Commands

The following lists the required parameters for operation. For all functions you must specify the device ID that can be found either manually or dynamically using the ```ListConnectedStandaDevices.exe``` executable.

e.g. ```StandaStepperMotorController.exe 1 [parameters]``` - specifies device 1.

##### Get Current Position
To get the current position of the device relative to its zero (or 'home') position, omit all parameters except the device id.

e.g. ```StandaStepperMotorController.exe 1``` - returns the current integer number of steps in its return code.

##### Power On
To turn the power supply of the stepper motor on append ```on``` to the executable at runtime.

e.g. ```StandaStepperMotorController.exe 1 on``` - turns the motor for controller 1 on.

## Python Modules
