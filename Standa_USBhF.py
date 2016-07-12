import subprocess


class ListDevices(object):

    @staticmethod
    def getDeviceID(id_code):
        fileLocation = "binaries\ListConnectedStandaDevices.exe " + str(id_code)
        ID = subprocess.Popen(fileLocation, creationflags=0x08000000)
        return ID.wait()


class ControllerInterface(object):
    device_id = 0

    def __init__(self, device_id):
        self.device_id = device_id

    def talk(self, parameterString = ""):
        fileLocation = "binaries\StandaStepperMotorController.exe " + \
            str(self.device_id) + " " + parameterString
        result = subprocess.Popen(fileLocation, creationflags=0x08000000)
        return result.wait()

    def powerOn(self):
        return self.talk("on")

    def powerOff(self):
        return self.talk("off")

    def step(self, steps):
        return self.talk("step " + str(steps))

    def goToPosition(self, position):
        return self.talk("goto " + str(position))

    def stop(self):
        return self.talk("stop")

    def setHome(self):
        return self.talk("setHome")

    def getPosition(self):
        return self.talk()

    def close(self):
        return self.talk("close")
