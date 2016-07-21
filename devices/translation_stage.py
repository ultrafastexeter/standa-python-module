from interface import Standa_USBhF
import os


class Standa_Translation_Stage(object):
    fudgeFactor = 0

    def __init__(self, controllerCode, micrometresPerWheelStep=1.25, reverse=False):
        self.micrometresPerPulse = (micrometresPerWheelStep * 200) / 1200
        self.pulsesPerMicrometre = 1 / self.micrometresPerPulse

        self.device_id = Standa_USBhF.ListDevices.getDeviceID(controllerCode)
        self.controller = Standa_USBhF.ControllerInterface(self.device_id, reverse)

        self.controllerCode = controllerCode
        self.powerOn()
        self.loadFudgeFactor()

    def loadFudgeFactor(self):
        try:
            file = open(os.path.join(os.path.dirname(__file__), 'fudgeData', str(self.controllerCode) + '.cal'), 'r')
            self.fudgeFactor = int(file.read())
            file.close()
        except:
            pass

    def saveFudgeFactor(self):
        file = open(os.path.join(os.path.dirname(__file__), 'fudgeData', str(self.controllerCode) + '.cal'), 'w')
        file.write(str(self.fudgeFactor))
        file.close()

    def powerOn(self):
        self.controller.powerOn()

    def powerOff(self):
        self.controller.powerOff()

    def setHome(self):
        self.controller.setHome()
        self.fudgeFactor = self.controller.getPosition()
        self.saveFudgeFactor()

    def goHome(self):
        self.controller.goToPosition(0 + self.fudgeFactor)

    def getRawPosition(self):
        pulses = self.controller.getPosition()
        return pulses * self.micrometresPerPulse

    def getPosition(self):
        pulses = self.controller.getPosition() + self.fudgeFactor
        return pulses * self.micrometresPerPulse

    def setPosition(self, micrometres):
        position = micrometres * self.pulsesPerMicrometre + self.fudgeFactor
        self.controller.goToPosition(int(position))

    def step(self, micrometres):
        pulses = micrometres * self.pulsesPerMicrometre
        self.controller.step(int(pulses))
