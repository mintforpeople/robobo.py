import json
from utils.message import Message
from utils.IR import IR

from processors import AbstractProcessor


class RobProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["IRS","BAT-BASE","BAT-PHONE","WHEELS","UNLOCK-MOVE"]

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
        elif (name == "UNLOCK-MOVE"):
            print("Unlock")
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






