from remotelib import Remote
from utils.Wheels import Wheels
from utils.IR import IR
import time

class Robobo:
    """

    """
    def __init__(self, ip):
        self.rem = Remote(ip)

    def connect(self):
        self.rem.wsStartup()

    def disconnect(self):
        self.rem.disconnect()

    def pause(self, seconds):
        time.sleep(seconds)

    def moveWheelsByTime(self, rSpeed, lSpeed, duration, wait = True):
        if wait:
            self.rem.moveWheelsWait(rSpeed, lSpeed, duration)

        else:
            self.rem.moveWheels(rSpeed, lSpeed, duration)

    def moveWheels(self, rSpeed, lSpeed):
            self.rem.moveWheels(rSpeed, lSpeed, 100000)

    def stopMotors(self):
        self.rem.moveWheels(0,0,1)

    def moveWheelsByDegree(self, wheel, degrees, speed, wait = True):
        if wait:
            self.rem.moveWheelsByDegreeWait(wheel,degrees,speed)

        else:
            self.rem.moveWheelsByDegree(wheel, degrees, speed)

    def movePanTo(self, degrees, speed, wait = True):
        if wait:
            self.rem.movePanWait(degrees, speed)

        else:
            self.rem.movePan(degrees, speed)

    def moveTiltTo(self, degrees, speed, wait = True):
        if wait:
            self.rem.moveTiltWait(degrees, speed)

        else:
            self.rem.moveTilt(degrees, speed)


    def setLedColorTo(self, led, color):
        self.rem.setLedColor(led, color)

    def resetWheelEncoders(self):
        self.rem.resetEncoders()

    def playNote(self, note, duration, wait = True):
        self.rem.playNote(note, duration,wait)

    def playSound(self, sound):
        self.rem.playEmotionSound(sound)

    def sayText(self, speech, wait = True):
        self.rem.talk(speech, wait)

    def resetClapCounter(self):
        self.rem.resetClaps()

    def resetTapSensor(self):
        self.rem.resetTap()

    def resetFlingSensor(self):
        self.rem.resetFling()

    def resetColorBlobs(self):
        self.rem.resetBlobs()

    def resetFaceSensor(self):
        self.rem.resetFace()

    def setEmotionTo(self, emotion):
        self.rem.setEmotionTo(emotion)

    def setActiveBlobs(self, red, green, blue, custom):
        self.rem.configureBlobTracking(red, green, blue, custom)


    def readClapCounter(self):
        return self.rem.state.claps

    def readLastNote(self):
        return self.rem.state.lastNote

    def readIRSensor(self, id):
        if self.rem.state.irs == []:
            return 0
        else:
            return int(self.rem.state.irs[id.value])

    def readAllIRSensor(self):
        return  self.rem.state.irs

    def readColorBlob(self, color):
        return self.rem.state.blobs[color]

    def readAllColorBlobs(self):
        return self.rem.state.blobs

    def readQR(self):
        return self.rem.state.qr

    def readOrientationSensor(self, axis):
        if axis == "yaw":
            return self.rem.state.yaw
        elif axis == "pitch":
            return self.rem.state.pitch
        elif axis == "roll":
            return self.rem.state.roll

    def readAccelerationSensor(self, axis):
        if axis == "x":
            return self.rem.state.accelx
        elif axis == "y":
            return self.rem.state.accely
        elif axis == "z":
            return self.rem.state.accelz

    def readTapSensor(self, axis):
        if axis == "x":
            return self.rem.state.tapx
        elif axis == "y":
            return self.rem.state.tapy

    def readPanPosition(self):
        return self.rem.state.panPos

    def readTiltPosition(self):
        return self.rem.state.tiltPos

    def readWheelPosition(self, wheel):
        if wheel.value == Wheels.R:
            return self.rem.state.wheelPosR
        elif wheel.value == Wheels.L:
            return self.rem.state.wheelPosL
        else:
            print("Wheel id not valid")
            return 0

    def readWheelSpeed(self, wheel):
        if wheel.value == Wheels.R:
            return self.rem.state.wheelSpeedR
        elif wheel.value == Wheels.L:
            return self.rem.state.wheelSpeedL
        else:
            print("Wheel id not valid")
            return 0

    def readFlingAngle(self):
        return self.rem.state.flingAngle

    def readFlingDistance(self):
        return self.rem.state.flingDistance

    def readFlingTime(self):
        return self.rem.state.flingTime

    def readBatteryLevel(self, device):
        if device == "phone":
            return self.rem.state.phoneBattery
        else:
            return self.rem.state.baseBattery

    def readNoiseLevel(self):
        return self.rem.state.noise

    def readBrightnessSensor(self):
        return self.rem.state.brightness

    def readFaceSensor(self):
        return self.rem.state.face

    def whenClapIsDetected(self, callback):
        self.rem.setClapCallback(callback)

    def whenANoteIsDetected(self, callback):
        self.rem.setNoteCallback(callback)

    def whenSpeechEnds(self, callback):
        self.rem.setTalkCallback(callback)

    def whenANewFaceIsDetected(self, callback):
        self.rem.setFaceCallback(callback)

    def whenANewColorBlobIsDetected(self, callback):
        self.rem.setBlobCallback(callback)

    def whenANewQRCodeIsDetected(self, callback):
        self.rem.setNewQRCallback(callback)

    def whenATapIsDetected(self, callback):
        self.rem.setTapCallback(callback)

    def whenAFlingIsDetected(self, callback):
        self.rem.setFlingCallback(callback)

    def whenAFaceIsLost(self, callback):
        self.rem.setLostFaceCallback(callback)

    def whenAQRCodeIsDetected(self, callback):
        self.rem.setQRCallback(callback)

    def whenAQRCodeIsLost(self, callback):
        self.rem.setLostQRCallback(callback)

    def changeStatusFrequency(self, frequency):
        self.rem.changeStatusFrequency(frequency)

