from robobopy.processors.AbstractProcessor import AbstractProcessor
from robobopy.utils.Message import Message


class CommandProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = []

    def sendGenericCommand(self, tag, parameters):
        name = tag
        id = self.state.getId()
        values = parameters
        return Message(name, values, id)


        

