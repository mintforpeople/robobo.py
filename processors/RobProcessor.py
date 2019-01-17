import json
from utils.Message import Message
from utils.IR import IR
from utils.Wheels import Wheels

from processors.AbstractProcessor import AbstractProcessor


class RobProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["IRS","LED","BAT-BASE","BAT-PHONE","WHEELS","UNLOCK-MOVE","UNLOCK-DEGREES"]

    def process(self, status):

        name = status["name"]
        value = status["value"]
        if (name == "WHEELS"):
            self.state.wheelPosR = int(value["wheelPosR"])
            self.state.wheelPosL = int(value["wheelPosL"])
            self.state.wheelSpeedR = int(value["wheelSpeedR"])
            self.state.wheelSpeedL = int(value["wheelSpeedL"])

        elif (name == "IRS"):
            self.state.irs = value
            for element in IR:
                self.state.irs[element] =  int(self.state.irs[element])

        elif (name == "LEDS"):
            self.state.leds = value

        elif (name == "UNLOCK-MOVE"):
            self.state.wheelLock = False

        elif (name == "BAT-BASE"):
            self.state.baseBattery = int(value["level"])
            print(self.state.baseBattery)

        elif (name == "BAT-PHONE"):  #
            self.phoneBattery = int(value["level"])
            print(self.state.phoneBattery)


    def moveWheelsSeparated(self,speedL, speedR, time):
        name = "MOVE"
        values= {"lspeed":speedL,
                 "rspeed":speedR,
                 "time":time}
        id = self.state.getId()

        return Message(name,values,id)

    def moveWheelsSeparatedWait(self,speedL, speedR, time, callback):
        name = "MOVE-BLOCKING"
        id = self.state.getId()
        values= {"lspeed":speedL,
                 "rspeed":speedR,
                 "time":time,
                 "blockid":id}

        return Message(name,values,id)

    def moveWheelsByDegree(self, wheel, degrees, speed):
        name = "MOVEBY-DEGREES"
        id = self.state.getId()
        values = {"wheel": wheel.value,
                  "degrees": degrees,
                  "speed": speed,
                  "blockid": id}

        return Message(name, values, id)

    def resetEncoders(self):

        name = "RESET-WHEELS"
        id = self.state.getId()
        values = {}

        return Message(name, values, id)

    def setLedColor(self, led, color):
        name = "SET-LEDCOLOR"
        id = self.state.getId()
        values = {"led": led.value,
                  "color": color.value}

        return Message(name, values, id)
