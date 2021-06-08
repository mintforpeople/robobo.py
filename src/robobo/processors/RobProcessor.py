from robobo.processors.AbstractProcessor import AbstractProcessor
from robobo.utils.Message import Message
from robobo.utils.IR import IR




class RobProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["IRS","LED","BAT-BASE","WHEELS","UNLOCK-MOVE","UNLOCK-DEGREES"]

    def process(self, status):
        name = status["name"]
        value = status["value"]
        if name == "WHEELS":
            self.state.wheelPosR = int(value["wheelPosR"])
            self.state.wheelPosL = int(value["wheelPosL"])
            self.state.wheelSpeedR = int(value["wheelSpeedR"])
            self.state.wheelSpeedL = int(value["wheelSpeedL"])
            self.state.lastWheelsTimestamp = int(value["timestamp"])

        elif name == "IRS":
            self.state.irs = value
            del self.state.irs['null']
            for element in IR:
                self.state.irs[element] =  int(self.state.irs[element])

        elif name == "LEDS":
            self.state.leds = value

        elif name == "UNLOCK-MOVE":
            self.state.wheelLock = False

        elif name == "BAT-BASE":
            self.state.baseBattery = int(value["level"])


    def moveWheelsSeparated(self,speedL, speedR, time):
        name = "MOVE"
        values= {"lspeed":speedL,
                 "rspeed":speedR,
                 "time":time}
        id = self.state.getId()

        return Message(name, values, id)

    def moveWheelsSeparatedWait(self,speedL, speedR, time):
        name = "MOVE-BLOCKING"
        id = self.state.getId()
        values= {"lspeed":speedL,
                 "rspeed":speedR,
                 "time":time,
                 "blockid":id}

        return Message(name, values, id)

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

    def changeStatusFrequency(self, frequency):
        name = "SET-SENSOR-FREQUENCY"
        id = self.state.getId()
        values = {"frequency":frequency.value}

        return Message(name, values, id)
