from robobopy.processors.AbstractProcessor import AbstractProcessor
from robobopy.utils.Message import Message
from robobopy.utils.Speech import Speech


class SpeechProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)

        self.speechCallback = None

        self.callbacklocks = {"speech": False }

        self.callbacks = {"speech": None }

        self.supportedMessages = ["SPEECH", "REGISTERED-PHRASES"]

    def process(self, status):
        name = status["name"]
        value = status["value"]
        if (name == "SPEECH"):  #
            self.state.lastSpeech = Speech(value["message"], value["recognized"].split(","), bool(value["final"]))
            self.runCallback("speech")
        elif (name == "REGISTERED-PHRASES"):  #
            self.state.registeredSpeechPhrases = value["phrases"].split(",")
    
    def startSpeechDetection(self):
        name = "START-SPEECH-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopSpeechDetection(self):
        name = "STOP-SPEECH-DETECTION"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)
    
    def registerSpeechPhrase(self, phrase):
        name = "SPEECH-ADD-PHRASE"
        values = {"phrase": phrase }
        id = self.state.getId()

        return Message(name, values, id)

    def removeSpeechPhrase(self, phrase):
        name = "SPEECH-REMOVE-PHRASE"
        values = {"phrase": phrase }
        id = self.state.getId()

        return Message(name, values, id)

    def detectAnySpeech(self):
        name = "SPEECH-DETECT-ANY"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def detectSpeechPhrasesOnly(self):
        name = "SPEECH-DETECT-PHRASES-ONLY"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)