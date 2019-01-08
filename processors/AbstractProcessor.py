

class AbstractProcessor:
    def __init__(self, state):
        self.state = state
        self.supportedMessages = []

    def canProcess(self, msg):
        return msg in self.supportedMessages

    def process(self, status):
        name = status["name"]
        value = status["value"]