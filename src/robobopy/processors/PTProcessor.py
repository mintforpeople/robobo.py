from robobopy.processors.AbstractProcessor import AbstractProcessor
from robobopy.utils.Message import Message


class PTProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["PAN","TILT","UNLOCK-PAN","UNLOCK-TILT"]

        self._panUpperLimit  = 343
        self._panLowerLimit  = 11
        self._tiltUpperLimit = 105
        self._tiltLowerLimit = 7

    def process(self, status):
        name = status["name"]
        value = status["value"]

        if (name == "PAN"):
            self.state.panPos = self.internalAngleToExternal(int(value["panPos"]))
            self.state.lastPanTimestamp = int(value["timestamp"])


        elif (name == "TILT"):
            self.state.tiltPos = int(value["tiltPos"])
            self.state.lastTiltTimestamp = int(value["timestamp"])


        elif (name == "UNLOCK-PAN"):
            self.state.panLock = False

        elif (name == "UNLOCK-TILT"):
            self.state.tiltLock = False

    def canProcess(self, msg):
        return msg in self.supportedMessages


    def movePan(self, pos, speed):
        name = "MOVEPAN"
        id = self.state.getId()
        values = {"pos":self.panBounds(self.externalAngleToInternal(pos)),
                  "speed": speed}

        return Message(name, values, id)

    def moveTilt(self, pos, speed):
        name = "MOVETILT"
        id = self.state.getId()
        values = {"pos":self.tiltBounds(pos),
                  "speed": speed}

        return Message(name, values, id)

    def movePanWait(self, pos, speed):
        name = "MOVEPAN-BLOCKING"
        id = self.state.getId()
        values = {"pos":self.panBounds(self.externalAngleToInternal(pos)),
                  "speed": speed,
                  "blockid": id}

        return Message(name, values, id)

    def moveTiltWait(self, pos, speed):
        name = "MOVETILT-BLOCKING"
        id = self.state.getId()
        values = {"pos":self.tiltBounds(pos),
                  "speed": speed,
                  "blockid": id}

        return Message(name, values, id)

    def panBounds(self, angle):
        if angle > self._panUpperLimit:
            return self._panUpperLimit

        elif angle < self._panLowerLimit:
            return self._panLowerLimit

        else:
            return angle

    def tiltBounds(self, angle):
        if angle > self._tiltUpperLimit:
            return self._tiltUpperLimit

        elif angle < self._tiltLowerLimit:
            return self._tiltLowerLimit

        else:
            return angle

    def externalAngleToInternal(self, angle):
        return angle+180


    def internalAngleToExternal(self, angle):
        return angle-180