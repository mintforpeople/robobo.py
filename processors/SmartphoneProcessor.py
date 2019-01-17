from processors.AbstractProcessor import AbstractProcessor
from utils import Emotions
from utils.Message import Message

class SmartphoneProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["ORIENTATION","ACCELERATION","AMBIENTLIGHT", "BAT-PHONE", "TAP", "FLING", "EMOTION"]

    def process(self, status):

        name = status["name"]
        value = status["value"]
        if (name == "ORIENTATION"):
            self.state.yaw = int(value["yaw"])
            self.state.pitch = int(value["pitch"])
            self.state.roll = int(value["roll"])

        elif (name == "ACCELERATION"):
            self.state.accelx = int(value["xaccel"])
            self.state.accely = int(value["yaccel"])
            self.state.accelz = int(value["zaccel"])

        elif (name == "AMBIENTLIGHT"):
            self.state.brightness = int(value["level"])

        elif (name == "BAT-PHONE"):
            self.state.phoneBattery = int(value["level"])

        elif (name == "TAP"):
            self.state.tapx = int(value["coordx"])
            self.state.tapy = int(value["coordy"])

        elif (name == "FLING"):
            self.state.flingangle = int(value["angle"])
            self.state.flingtime = int(value["time"])
            self.state.flingdistance = int(value["distance"])

        elif (name == "EMOTION"):
            self.state.emotion = value["emotion"]

    def setEmotion(self, emotion):
        name = "SET-EMOTION"
        id = self.state.getId()
        values = {"emotion": emotion.value}

        return Message(name, values, id)