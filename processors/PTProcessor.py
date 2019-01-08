from processors import AbstractProcessor
class PTProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["PAN","TILT"]

    def process(self, status):
        name = status["name"]
        value = status["value"]

        if (name == "PAN"):
            self.state.panPos = value["panPos"]

        elif (name == "TILT"):
            self.state.tiltPos = value["tiltPos"]

    def canProcess(self, msg):
        return msg in self.supportedMessages


