from . import translation_stage


class Delay_Line(object):
    speed_of_light = float(299792458)

    def __init__(self, controller_code, micrometres_per_step=1.25, reverse=False):
        self.stage = translation_stage.Standa_Translation_Stage(controller_code, micrometres_per_step, reverse)

    def getDistanceFromDelay(self, delay_ps):
        delay_s = delay_ps * 1e-12
        distance_m = delay_s * self.speed_of_light
        distance_um = distance_m * 1e6
        return distance_um

    def getDelayFromDistance(self, distance_um):
        distance_m = distance_um * 1e-6
        delay_s = distance_m / self.speed_of_light
        delay_ps = delay_s * 1e12
        return delay_ps

    def setDelay(self, delay_ps):
        position = self.getDistanceFromDelay(delay_ps) / 2
        self.stage.setPosition(position)

    def getDelay(self):
        distance_um = self.stage.getPosition()
        return self.getDelayFromDistance(distance_um) * 2

    def changeBy(self, delay_ps):
        distance_um = self.getDistanceFromDelay(delay_ps) / 2
        self.stage.step(distance_um)

    def setHome(self):
        self.stage.setHome()

    def reset(self):
        self.stage.goHome()
