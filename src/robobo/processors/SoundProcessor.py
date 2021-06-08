from robobo.processors.AbstractProcessor import AbstractProcessor
from robobo.utils.Message import Message


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
