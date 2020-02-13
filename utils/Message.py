class Message:
    def __init__(self, name, parameters, id):
        self.name = name
        self.parameters = parameters
        self.id = id

    def encode(self):
        st = "{\"name\":"
        st += "\"" + self.name + "\","

        st += "\"parameters\":{"

        for key in self.parameters.keys():
            st += "\"" + key + "\":" + "\"" + str(self.parameters[key]) + "\","

        if st[-1] !="{":
            st = st[:-1]

        st += "}, \"id\":\"" + str(self.id) + "\"}"

        return st
