import subprocess
import platform
import os


class ListDevices(object):

    @staticmethod
    def getDeviceID(id_code):
        if platform.system() == "Windows":
            fileLocation = os.path.join(os.path.dirname(__file__), 'binaries', 'ListConnectedStandaDevices.exe') + ' ' + str(id_code)
            ID = subprocess.Popen(fileLocation, creationflags=0x08000000)
            return ID.wait()
        else:
            print "Not Windows - Returning " + str(id_code)
            return id_code


class ControllerInterface(object):
    device_id = 0

    def __init__(self, device_id, reverse=False):
        self.device_id = device_id
        self.reverse = reverse
        self.windows = False
        if platform.system() == "Windows":
            self.windows = True

    def talk(self, parameterString=""):
        if self.windows:
            fileLocation = os.path.join(os.path.dirname(__file__), 'binaries', 'StandaStepperMotorController.exe') + ' ' + str(self.device_id) + ' ' + parameterString
            result = subprocess.Popen(fileLocation, creationflags=0x08000000)
            return result.wait()
        else:
            print "Motor Instruction: " + str(self.device_id) + " " + parameterString
            return 0

    def powerOn(self):
        return self.talk("on")

    def powerOff(self):
        return self.talk("off")

    def step(self, steps):
        if self.reverse:
            steps = steps * -1
        return self.talk("step " + str(steps))

    def goToPosition(self, position):
        if self.reverse:
            position = position * -1
        return self.talk("goto " + str(position))

    def stop(self):
        return self.talk("stop")

    def setHome(self):
        return self.talk("setHome")

    def getPosition(self):
        return self.talk()

    def close(self):
        return self.talk("close")
