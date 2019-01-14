from remotelib import Remote
from utils import Wheels, IR
import time
class Robobo:
    def __init__(self, ip):
        self.rem = Remote(ip)

    def connect(self):
        self.rem.wsStartup()

    def wait(self, seconds):
        time.sleep(seconds)

    def moveWheels(self, rSpeed, lSpeed, duration, wait = True):
        if wait:
            self.rem.moveWheelsWait(rSpeed, lSpeed, duration)
        else:
            self.rem.moveWheels(rSpeed, lSpeed, duration)

    def moveWheelsByDegree(self, wheel, degrees, speed, wait = True):
        if wait:
            self.rem.moveWheelsByDegreeWait(wheel,degrees,speed)
        else:
            self.rem.moveWheelsByDegree(wheel, degrees, speed)

    def movePan(self, degrees, speed, wait = True):
        if wait:
            self.rem.movePanWait(degrees, speed)
        else:
            self.rem.movePan(degrees, speed)

    def moveTilt(self, degrees, speed, wait = True):
        if wait:
            self.rem.moveTiltWait(degrees, speed)
        else:
            self.rem.moveTilt(degrees, speed)

    def getIR(self, id):
        return self.rem.state.irs[id.value]