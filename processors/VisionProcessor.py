
from processors import AbstractProcessor

class VisionProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["QRCODE","FACE","BLOB","QRCODEAPPEAR","QRCODELOST"]

    def process(self, status):
        name = status["name"]
        value = status["value"]

        if (name == "FACE"):
            self.state.facex = int(value["coordx"])
            self.state.facey = int(value["coordy"])
            self.state.facedist = int(value["distance"])


        elif (name == "BLOB"):
            print(status)
            self.state.blobs[value["color"]].posx = int(value["posx"])

            self.state.blobs[value["color"]].posy = int(value["posy"])

            self.state.blobs[value["color"]].size = int(value["size"])

        # elif (name == "QRCODEAPPEAR"):
        # Callback here

        # elif (name == "QRCODELOST"):
        # Callback here




