# Python Modules for Standa 8SMC1-USBhF

Python modules for controlling Standa 8SMC1-USBhF Motor Controller connected to a Windows PC over USB. Developed by Sam Hutchings whilst working on a student Summer Research Project in the Physics department at the [University of Exeter](http://emps.exeter.ac.uk/physics-astronomy/).

## Dependencies
* Windows Only - Tested on Windows 7 and 10
* MicroSMC - included in downloads available from the product page on Standa's website [here](http://www.standa.lt/products/catalog/motorised_positioners?item=175). Uses the included *USMCDLL.dll*.

## Binaries
The ```binaries``` folder contains two executables:

### ```ListConnectedStandaDevices.exe```

Prints the currently connected Standa devices connected to the system to the command line, showing the current device ID and the serial number for each device. If the last four characters are entered as the first parameter, the program will return the device id of that controller as its return code, provided the device is connected to the system.

e.g. ```ListConnectedStandaDevices.exe 4298``` - returns the device ID of that controller using as the program's return code.

### ```StandaStepperMotorController.exe```

Interfaces with the motor controller. Can be provided with a variety of parameters to execute operations. A short delay is built into each command so they will in most cases return after *100ms*. This is to prevent the execution of commands dependent on a change a previous command makes, executing before that change has been made, reducing the likelihood of unexpected behaviours which emerged during testing.

#### Commands

The following lists the required parameters for operation. For all functions you must specify the device ID that can be found either manually or dynamically using the ```ListConnectedStandaDevices.exe``` executable.

e.g. ```StandaStepperMotorController.exe 1 [parameters]``` - specifies device 1.

##### Get Current Position
To get the current position of the device relative to its zero (or 'home') position, omit all parameters except the device id.

e.g. ```StandaStepperMotorController.exe 1``` - returns the current integer number of steps in its return code.

##### Power On
To turn the power supply of the stepper motor on append ```on``` to the executable at runtime.

e.g. ```StandaStepperMotorController.exe 1 on``` - turns the motor for controller 1 on.

##### Power Off
To turn the power supply of the stepper motor on append ```off``` to the executable at runtime. This allows for manual adjustment with the thumb screw.

e.g. ```StandaStepperMotorController.exe 1 off``` - turns the motor for controller 1 off.

##### Step and GoTo
There are two commands that can be used to move the stage. The first is the ```step``` command, which moves the motor a number of steps relative to its current position. This is called by appending ```step``` and the integer number of steps you wish to take to the execution command.

e.g. ```StandaStepperMotorController.exe 1 step 10``` - moves the motor connected to controller 1 ten steps forward.

The second method, ```goto``` is an absolute position command. When used, this moves the stage the provided number of steps, relative to the home position. The structure of execution is identical to the ```step``` command.

e.g. ```StandaStepperMotorController.exe 1 goto 20``` - moves the motor connected to controller to the position twenty steps from the home position.

Both commands return when the move is complete, and both can take a negative integer value.

##### Set Home
This command resets the home (or zero) position of the motor to be the current position. All subsequent moves will be relative to this location. This is achieved by appending ```setHome``` to the start command.

e.g. ```StandaStepperMotorController.exe 1 setHome``` - sets the current position of the motor connected to controller 1 to be the motor's home position.

##### Stop
The stop command immediately stops the movement of the motor.

e.g. e.g. ```StandaStepperMotorController.exe 1 stop``` - stops the motor connected to controller 1.

##### Close
To close the connection with the USMCDLL.dll module to allow it close, append ```close``` to the end of the execution command.

e.g. ```StandaStepperMotorController.exe 1 close```


## Python Modules
