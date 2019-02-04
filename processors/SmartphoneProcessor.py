from processors.AbstractProcessor import AbstractProcessor
from utils import Emotions
from utils.Message import Message

class SmartphoneProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["ORIENTATION","ACCELERATION","AMBIENTLIGHT", "BAT-PHONE", "TAP", "FLING", "EMOTION"]

        self.tapCallback = None
        self.flingCallback = None

        self.callbacklocks = {"tap": False,
                              "fling": False}

        self.callbacks = {"tap":  None,
                          "fling":None}

    def process(self, status):

        name = status["name"]
        value = status["value"]
        print(name)
        if (name == "ORIENTATION"):
            self.state.yaw =   float(value["yaw"])
            self.state.pitch = float(value["pitch"])
            self.state.roll =  float(value["roll"])

        elif (name == "ACCELERATION"):
            self.state.accelx = float(value["xaccel"])
            self.state.accely = float(value["yaccel"])
            self.state.accelz = float(value["zaccel"])

        elif (name == "AMBIENTLIGHT"):
            self.state.brightness = int(value["level"])

        elif (name == "BAT-PHONE"):
            self.state.phoneBattery = int(value["level"])

        elif (name == "TAP"):
            self.state.tapx = int(value["coordx"])
            self.state.tapy = int(value["coordy"])
            self.runCallback("tap")

        elif (name == "FLING"):
            self.state.flingAngle =    float(value["angle"])
            self.state.flingTime =     float(value["time"])
            self.state.flingDistance = float(value["distance"])
            self.runCallback("fling")
        elif (name == "EMOTION"):
            self.state.emotion = value["emotion"]

    def setEmotion(self, emotion):
        name = "SET-EMOTION"
        id = self.state.getId()
        values = {"emotion": emotion.value}

        return Message(name, values, id)

    def resetTap(self):
        self.state.tapx = 0
        self.state.tapy = 0

    def resetFling(self):
        self.state.flingAngle = 0
        self.state.flingDistance = 0
        self.state.flingTime = 0