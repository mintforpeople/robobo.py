from remotelib import Remote
from utils.Wheels import Wheels
from utils.IR import IR
import time

class Robobo:
    def __init__(self, ip):
        self.rem = Remote(ip)

    def connect(self):
        self.rem.wsStartup()

    def wait(self, seconds):
        time.sleep(seconds)

    def moveWheels(self, rSpeed, lSpeed, duration=30000, wait = True):
        if wait:
            self.rem.moveWheelsWait(rSpeed, lSpeed, duration)
        else:
            self.rem.moveWheels(rSpeed, lSpeed, duration)

    def stopMotors(self):
        self.moveWheels(0,0,1,False)

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

    def getClaps(self):
        return self.rem.state.claps

    def getIR(self, id):
        if self.rem.state.irs == []:
            return 0
        else:
            return self.rem.state.irs[id.value]

    def getBlob(self, color):
        return  self.rem.state.blobs[color]

    def getQR(self):
        return self.rem.state.qr

    def getOrientation(self,axis):
        if axis == "yaw":
            return self.rem.state.yaw
        elif axis == "pitch":
            return self.rem.state.pitch
        elif axis == "roll":
            return self.rem.state.roll

    def getAcceleration(self,axis):
        if axis == "x":
            return self.rem.state.accelx
        elif axis == "y":
            return self.rem.state.accely
        elif axis == "z":
            return self.rem.state.accelz

    def getTap(self,axis):
        if axis == "x":
            return self.rem.state.tapx
        elif axis == "y":
            return self.rem.state.tapy

    def getPanPos(self):
        return self.rem.state.panPos

    def getTiltPos(self):
        return self.rem.state.tiltPos

    def getWheelPos(self, wheel):
        if wheel.value == Wheels.R:
            return self.rem.state.wheelPosR
        elif wheel.value == Wheels.L:
            return self.rem.state.wheelPosL
        else:
            print("Wheel id not valid")
            return 0

    def getWheelSpeed(self, wheel):
        if wheel.value == Wheels.R:
            return self.rem.state.wheelSpeedR
        elif wheel.value == Wheels.L:
            return self.rem.state.wheelSpeedL
        else:
            print("Wheel id not valid")
            return 0

    def getFlingAngle(self):
        return self.rem.state.flingAngle

    def getFlingDistance(self):
        return self.rem.state.flingDistance

    def getFlingTime(self):
        return self.rem.state.flingTime

    def getPhoneBattery(self):
        return self.rem.state.phoneBattery

    def getBaseBattery(self):
        return self.rem.state.baseBattery

    def getNoiseLevel(self):
        return self.rem.state.noise

    def getFace(self):
        return self.rem.state.face

    def onClap(self, callback):
        self.rem.setClapCallback(callback)

    def onNote(self, callback):
        self.rem.setNoteCallback(callback)

    def onTalk(self, callback):
        self.rem.setTalkCallback(callback)

    def onFace(self, callback):
        self.rem.setFaceCallback(callback)

    def onBlob(self, callback):
        self.rem.setBlobCallback(callback)

    def onQR(self, callback):
        self.rem.setQRCallback(callback)

    def onTap(self, callback):
        self.rem.setTapCallback(callback)

    def onFling(self, callback):
        self.rem.setFlingCallback(callback)


