from robobopy.utils.Blob import Blob
from robobopy.utils.DetectedObject import DetectedObject
from robobopy.utils.Face import Face
from robobopy.utils.Lanes import LanePro, LaneBasic
from robobopy.utils.Lines import Lines
from robobopy.utils.QRCode import QRCode
from robobopy.utils.Tag import Tag
from robobopy.utils.Speech import Speech


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
        self.lastPanTimestamp = 0
        self.tiltPos = 0
        self.lastTiltTimestamp = 0
        self.blobs = {

            "red": Blob("red", 0, 0, 0, -1, -1),
            "green": Blob("green", 0, 0, 0, -1, -1),
            "blue": Blob("blue", 0, 0, 0, -1, -1),
            "custom": Blob("custom", 0, 0, 0, -1, -1)}


        self.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None", 0)

        self.lastNote = ''
        self.lastNoteDuration = 0

        self.wheelPosR = 0
        self.wheelPosL = 0
        self.wheelSpeedR = 0
        self.wheelSpeedL = 0
        self.lastWheelsTimestamp = 0


        self.wheelLock = False
        self.panLock = False
        self.tiltLock = False
        self.degreesLock = False
        self.talkLock = False

        self.emotion = "normal"

        self.detectedObject = DetectedObject(0, 0, 0, 0, 0.0, "", 0)


        self.tag = Tag(0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "", 0)

        self.lines = Lines([], 0)
        self.lanePro = LanePro(0, 0, 0, 0, 0, 0, [], 0)
        self.laneBasic = LaneBasic(0, 0, 0, 0, 0)

        self.lastLaneTimestamp = 0
        self.lastLineTimestamp = 0

        self.lastSpeech = Speech("", [], True)
        self.registeredSpeechPhrases = []


    def getId(self):
        retId = self.id
        self.id += 1
        return retId

    def resetSensors(self):
        self.claps = 0

        self.irs = []
        self.lastIrTimestamp = 0

        self.baseBattery = 0
        self.phoneBattery = 0
        self.lastBatteryTimestamp = 0

        self.face = Face(0, 0, 0)

        self.tapx = 0
        self.tapy = 0
        self.lastTapTimestamp = 0

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
        self.lastPanTimestamp = 0
        self.tiltPos = 0
        self.lastTiltTimestamp = 0

        self.blobs = {
            "red": Blob("red", 0, 0, 0, 0, 0),
            "green": Blob("green", 0, 0, 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0, 0, 0),

        }

        self.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None", 0)

        self.detectedObject = DetectedObject(0, 0, 0, 0, 0.0, "", 0)
        self.tag = Tag(0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "", 0)

        self.lines = Lines([], 0)
        self.lastLineTimestamp = 0
        self.lanePro = LanePro(0, 0, 0, 0, 0, 0, [], 0)
        self.laneBasic = LaneBasic(0, 0, 0, 0, 0)
        self.lastLaneTimestamp = 0

        self.lastNote = 0
        self.lastNoteDuration = 0
        self.lastNoteTimestamp = 0

        self.wheelPosR = 0
        self.wheelPosL = 0
        self.wheelSpeedR = 0
        self.wheelSpeedL = 0
        self.lastWheelsTimestamp = 0

        self.emotion = "normal"
