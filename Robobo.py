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
        if self.rem.state.irs == []:
            return 0
        else:
            return self.rem.state.irs[id.value]

    def getBlob(self, color):
        return  self.rem.state.blobs[color]

    def setLedColor(self, led, color):
        self.rem.setLedColor(led, color)

    def resetWheels(self):
        self.rem.resetEncoders()

    def playNote(self, note, duration, wait = True):
        self.rem.playNote(note, duration,wait)

    def playEmotionSound(self, sound):
        self.rem.playEmotionSound(sound)

    def talk(self, speech, wait = True):
        self.rem.talk(speech, wait)

    def resetClaps(self):
        self.rem.resetClaps()

    def setEmotion(self, emotion):
        self.rem.setEmotion(emotion)

    def configureBlobTracking(self, red, green, blue, custom):
        self.rem.configureBlobTracking(red, green, blue, custom)
