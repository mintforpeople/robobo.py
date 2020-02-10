import json
from utils.Blob import Blob
from utils.DetectedObject import DetectedObject
from utils.QRCode import QRCode
from utils.Face import Face
from utils.Tag import Tag


class State:
    def __init__(self):
        self.id = 0

        self.noise = 0

        self.claps = 0

        self.irs = []
        self.leds = []

        self.baseBattery = 0
        self.phoneBattery = 0

        self.face = Face(0, 0, -1)

        self.tapx = 0
        self.tapy = 0

        self.flingAngle = 0
        self.flingTime = 0
        self.flingDistance = 0
        self.brightness = 0

        self.pitch = 0
        self.yaw = 0
        self.roll = 0

        self.accelx = 0
        self.accely = 0
        self.accelz = 0

        self.panPos = 0
        self.tiltPos = 0

        self.blobs = {
            "red": Blob("red", 0, 0, 0),
            "green": Blob("green", 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0)}

        self.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None")

        self.lastNote = ''
        self.lastNoteDuration = 0

        self.wheelPosR = 0
        self.wheelPosL = 0
        self.wheelSpeedR = 0
        self.wheelSpeedL = 0

        self.wheelLock = False
        self.panLock = False
        self.tiltLock = False
        self.degreesLock = False
        self.talkLock = False

        self.emotion = "normal"

        self.detectedObject = DetectedObject(0, 0, 0, 0, 0.0, "")
        self.tag = Tag(0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "")

    def getId(self):
        retId = self.id
        self.id += 1
        return retId

    def resetSensors(self):
        self.claps = 0

        self.irs = []

        self.baseBattery = 0
        self.phoneBattery = 0

        self.face = Face(0, 0, 0)

        self.tapx = 0
        self.tapy = 0

        self.flingAngle = 0
        self.flingTime = 0
        self.flingDistance = 0
        self.brightness = 0

        self.pitch = 0
        self.yaw = 0
        self.roll = 0

        self.accelx = 0
        self.accely = 0
        self.accelz = 0

        self.panPos = 0
        self.tiltPos = 0

        self.blobs = {
            "red": Blob("red", 0, 0, 0),
            "green": Blob("green", 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0),

        }

        self.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None")

        self.detectedObject = DetectedObject(0, 0, 0, 0, 0.0, "")
        self.tag = Tag(0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "")

        self.lastNote = 0
        self.lastNoteDuration = 0

        self.wheelPosR = 0
        self.wheelPosL = 0
        self.wheelSpeedR = 0
        self.wheelSpeedL = 0

        self.emotion = "normal"
