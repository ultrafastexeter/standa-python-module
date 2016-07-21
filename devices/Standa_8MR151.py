from interface import Standa_USBhF
import os


class Standa_8MR151(object):
    pulsesPerRev = 72000 * 4
    pulsesPerDegree = float(pulsesPerRev) / 360
    degreesPerPulse = 1.0 / pulsesPerDegree
    fudgeFactor = 0

    def __init__(self, controllerCode, reverse=True):
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
        self.controller.goToPosition(0 - self.fudgeFactor)

    def getRawAngle(self):
        pulses = self.controller.getPosition()
        return pulses * self.degreesPerPulse

    def getAngle(self):
        pulses = self.controller.getPosition() - self.fudgeFactor
        return pulses * self.degreesPerPulse

    def setAngle(self, angle):
        position = angle * self.pulsesPerDegree - self.fudgeFactor
        self.controller.goToPosition(int(position))

    def rotateBy(self, angle):
        pulses = angle * self.pulsesPerDegree
        self.controller.step(int(pulses))
