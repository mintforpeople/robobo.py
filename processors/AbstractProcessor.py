import threading

class AbstractProcessor:
    def __init__(self, state):
        self.state = state
        self.supportedMessages = []

    def canProcess(self, msg):
        return msg in self.supportedMessages

    def process(self, status):
        name = status["name"]
        value = status["value"]

    def runCallback(self,callback):
        if not callback == None:
            t = threading.Thread(target=callback)
            t.start()