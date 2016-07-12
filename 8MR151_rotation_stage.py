import Standa_USBhF


class Standa_8MR151(object):
    pulsesPerRev = 72000 * 4
    pulsesPerDegree = pulsesPerRev / 360
    degreesPerPulse = 1 / pulsesPerDegree

    def __init__(self, controllerCode):
        self.device_id = Standa_USBhF.ListDevices.getDeviceID(controllerCode)
        self.controller = Standa_USBhF.ControllerInterface(self.device_id)
        self.powerOn()

    def powerOn(self):
        self.controller.powerOn()

    def powerOff(self):
        self.controller.powerOff()

    def setHome(self):
        self.controller.setHome()

    def goHome(self):
        self.controller.goToPosition(0)

    def getAngle(self):
        pulses = self.controller.getPosition()
        return pulses * self.degreesPerPulse

    def setAngle(self, angle):
        position = angle * self.pulsesPerDegree
        self.controller.goToPosition(int(position))

    def rotateBy(self, angle):
        pulses = angle * self.pulsesPerDegree
        self.controller.step(int(pulses))
