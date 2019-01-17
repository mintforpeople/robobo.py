
from processors.AbstractProcessor import AbstractProcessor
from utils.Message import Message
from utils.QRCode import QRCode
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

        elif (name == "QRCODEAPPEAR"):

            self.state.qr = QRCode(int(value["coordx"]),
                             int(value["coordy"]),
                             int(value["distance"]),
                             int(value["p1x"]),
                             int(value["p1y"]),
                             int(value["p2x"]),
                             int(value["p2y"]),
                             int(value["p3x"]),
                             int(value["p3y"]))

        elif (name == "QRCODE"):
            self.state.qr = QRCode(int(value["coordx"]),
                             int(value["coordy"]),
                             int(value["distance"]),
                             int(value["p1x"]),
                             int(value["p1y"]),
                             int(value["p2x"]),
                             int(value["p2y"]),
                             int(value["p3x"]),
                             int(value["p3y"]))

        elif (name == "QRCODELOST"):
            self.state.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0)


    def configureBlobTracking(self, red, green, blue, custom):
        name = "CONFIGURE_BLOBTRACKING"
        id = self.state.getId()
        values = {"red": red,
                  "green": green,
                  "blue": blue,
                  "custom": custom}

        return Message(name, values, id)


