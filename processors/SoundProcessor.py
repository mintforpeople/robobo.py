from processors.AbstractProcessor import AbstractProcessor
from utils.Message import Message


class SoundProcessor(AbstractProcessor):
    def __init__(self, state, clapCallback):
        super().__init__(state)
        self.supportedMessages = ["NOTE", "CLAP", "UNLOCK-TALK", "NOISE"]
        self.clapCallback = clapCallback

    def process(self, status):

        name = status["name"]
        value = status["value"]

        if (name == "NOISE"):  #
            self.state.noise = float(value["level"])

        elif (name == "CLAP"):  #
            self.state.claps += 1
            self.clapCallback()
        elif (name == "NOTE"):
            self.state.lastNote = int(value["name"])
            self.state.lastNoteDuration = int(value["duration"])

        elif (name == "UNLOCK-TALK"):
            self.state.talkLock = False
    def playNote(self, index, duration):
        name = "MOVE"
        values = {"index": index,
                  "time": duration}
        id = self.state.getId()

        return Message(name, values, id)

    def playEmotionSound(self, sound):
        name = "SOUND"
        values = {"sound": sound}
        id = self.state.getId()

        return Message(name, values, id)

    def talk(self, speech):
        name = "TALK"
        values = {"text": speech}
        id = self.state.getId()

        return Message(name, values, id)

    def resetClaps(self):
        self.state.claps = 0
