class Message:
    """
    This class encapsulates messages to be sent to the Robobo
    Attributes:
        - name: Name of the message.
        - parameters: Dictionary containing the parameters contained in the message.
        - id: Message identifier.
    """
    def __init__(self, name, parameters, id):
        self.name = name
        self.parameters = parameters
        self.id = id

    def encode(self):
        """
        Encodes the message in JSON format.

        :return: Encoded message
        :rtype: str
        """
        st = "{\"name\":"
        st += "\"" + self.name + "\","

        st += "\"parameters\":{"

        for key in self.parameters.keys():
            st += "\"" + key + "\":" + "\"" + str(self.parameters[key]) + "\","

        if st[-1] !="{":
            st = st[:-1]

        st += "}, \"id\":\"" + str(self.id) + "\"}"

        return st
