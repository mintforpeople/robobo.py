import threading

class AbstractProcessor:
    def __init__(self, state):
        self.state = state
        self.supportedMessages = []
        self.callbacks = {}
        self.callbacklocks = {}

    def canProcess(self, msg):
        return msg in self.supportedMessages

    def process(self, status):
        name = status["name"]
        value = status["value"]

    def _wrapCallback(self, callback, callbackName):
        self.callbacklocks[callbackName] = True
        try:
            callback()
        finally:
            self.callbacklocks[callbackName] = False

    def runCallback(self, callbackName):
        callbackExists = self.callbacks.get(callbackName) is not None

        if callbackExists:
            if not self.callbacklocks.get(callbackName, False):
                t = threading.Thread(target=self._wrapCallback, args=[self.callbacks[callbackName], callbackName])
                t.daemon = True
                t.start()
            else:
                pass
