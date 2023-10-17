from robobopy.processors.AbstractProcessor import AbstractProcessor
from robobopy.utils.Message import Message


class SoundProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)

        self.clapCallback = None
        self.noteCallback = None
        self.talkCallback = None

        self.callbacklocks = {"clap": False,
                              "note": False,
                              "talk": False}

        self.callbacks = {"clap": None,
                          "note": None,
                          "talk": None}

        self.supportedMessages = ["NOTE", "CLAP", "UNLOCK-TALK", "NOISE"]

    def process(self, status):

        name = status["name"]
        value = status["value"]

        if (name == "NOISE"):  #
            self.state.noise = float(value["level"])

        elif (name == "CLAP"):  #
            self.state.claps += 1
            self.runCallback("clap")

        elif (name == "NOTE"):
            self.state.lastNote = value["name"]
            self.state.lastNoteDuration = int(value["duration"])
            self.runCallback("note")

        elif (name == "UNLOCK-TALK"):
            self.state.talkLock = False
            self.runCallback("talk")

    def playNote(self, index, duration):
        name = "PLAY-NOTE"
        values = {"index": index,
                  "time": duration}
        id = self.state.getId()

        return Message(name, values, id)

    def playEmotionSound(self, sound):
        name = "PLAY-SOUND"
        values = {"sound": sound.value}
        id = self.state.getId()

        return Message(name, values, id)

    def talk(self, speech):
        name = "TALK"
        values = {"text": speech}
        id = self.state.getId()

        return Message(name, values, id)

    def resetClaps(self):
        self.state.claps = 0

    # Stream related functions
    def startAudioStream(self):
        name = "START-AUDIOSTREAM"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)

    def stopAudioStream(self):
        name = "STOP-AUDIOSTREAM"
        id = self.state.getId()
        values = {}
        return Message(name, values, id)
    
    def setAudioStreamBitrate(self, bitrate):
        name = "SET-AUDIOSTREAM-SAMPLERATE"
        id = self.state.getId()
        values = {"bitrate": bitrate}
        return Message(name, values, id)
    
    def sendSyncAudio(self, syncId):
        name = "AUDIOSTREAM-SYNC"
        id = self.state.getId()
        values = {"id":syncId}
        return Message(name, values, id)
