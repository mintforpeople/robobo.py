import json
from objects.Blob import Blob


class State:
    def __init__(self):
        self.id = 0

        self.noise = 0

        self.claps = 0

        self.irs = []
        self.leds = []

        self.baseBattery = 0
        self.phoneBattery = 0

        self.facex = 0
        self.facey = 0
        self.facedist = 0

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

        self.blobPosx = 0
        self.blobPosy = 0
        self.blobSize = 0

        self.blobs = {
            "red": Blob("red", 0, 0, 0),
            "green": Blob("green", 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0)}

        self.lastNote = 0
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

    def getId(self):
        retId = self.id
        self.id += 1
        return retId

    def resetSensors(self):
        self.claps = 0

        self.irs = []

        self.baseBattery = 0
        self.phoneBattery = 0

        self.facex = 0
        self.facey = 0
        self.facedist = 0

        self.tapx = 0
        self.tapy = 0

        self.flingangle = 0
        self.flingtime = 0
        self.flingdistance = 0
        self.brightness = 0

        self.pitch = 0
        self.yaw = 0
        self.roll = 0

        self.accelx = 0
        self.accely = 0
        self.accelz = 0

        self.panPos = 0
        self.tiltPos = 0

        self.blobPosx = 0
        self.blobPosy = 0
        self.blobSize = 0

        self.blobs = {
            "red": Blob("red", 0, 0, 0),
            "green": Blob("green", 0, 0, 0),
            "blue": Blob("blue", 0, 0, 0),
            "custom": Blob("custom", 0, 0, 0),

        }

        self.lastNote = 0
        self.lastNoteDuration = 0

        self.wheelPosR = 0
        self.wheelPosL = 0
        self.wheelSpeedR = 0
        self.wheelSpeedL = 0

        self.emotion = "normal"

    def process(self, msg):

        status = json.loads(msg)
        print(status)
        name = status["name"]
        value = status["value"]

        if (name == "TAP"):
            self.tapx = int(value["coordx"])
            self.tapy = int(value["coordy"])

        elif (name == "FLING"):
            self.flingangle = int(value["angle"])
            self.flingtime = int(value["time"])
            self.flingdistance = int(value["distance"])

        elif (name == "AMBIENTLIGHT"):
            self.brightness = int(value)

        elif (name == "ORIENTATION"):
            self.pitch = int(value["pitch"])
            self.yaw = int(value["yaw"])
            self.roll = int(value["roll"])

        elif (name == "ACCELERATION"):
            self.accelx = int(value["accelx"])
            self.accely = int(value["accely"])
            self.accelz = int(value["accelz"])








        elif (name == "EMOTION"):
            self.emotion = value["emotion"]

        elif (name == "QRCODE"):
            self.qr = value

        # elif (name == "LED"):
        # this.led
