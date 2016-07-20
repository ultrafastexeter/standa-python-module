from ..interface import Standa_USBhF


class Standa_Translation_Stage(object):
    micrometresPerPulse = (1.25 * 200) / 1200
    pulsesPerMicrometre = 1 / micrometresPerPulse

    def __init__(self, controllerCode, micrometresPerWheelStep=1.25, reverse=False):
        self.micrometresPerPulse = (micrometresPerWheelStep * 200) / 1200
        self.pulsesPerMicrometre = 1 / self.micrometresPerPulse

        self.device_id = Standa_USBhF.ListDevices.getDeviceID(controllerCode)
        self.controller = Standa_USBhF.ControllerInterface(self.device_id, reverse)
        self.powerOn()

    def powerOn(self):
        self.controller.powerOn()

    def powerOff(self):
        self.controller.powerOff()

    def setHome(self):
        self.controller.setHome()

    def goHome(self):
        self.controller.goToPosition(0)

    def getPosition(self):
        pulses = self.controller.getPosition()
        return pulses * self.micrometresPerPulse

    def setPosition(self, micrometres):
        position = micrometres * self.pulsesPerMicrometre
        self.controller.goToPosition(int(position))

    def step(self, micrometres):
        pulses = micrometres * self.pulsesPerMicrometre
        self.controller.step(int(pulses))
