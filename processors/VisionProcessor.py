
from processors.AbstractProcessor import AbstractProcessor
from utils.Message import Message
from utils.QRCode import QRCode
from utils.Face import Face
class VisionProcessor(AbstractProcessor):
    def __init__(self, state):
        super().__init__(state)
        self.supportedMessages = ["QRCODE","FACE","BLOB","QRCODEAPPEAR","QRCODELOST"]


        self.callbacklocks={"qr": False,
                           "face": False,
                           "blob": False}

        self.callbacks={"qr": None,
                           "face": None,
                           "blob": None}

    def process(self, status):
        name = status["name"]
        value = status["value"]

        if (name == "FACE"):
            self.state.face = Face(int(value["coordx"]),int(value["coordy"]), int(value["distance"]))
            self.runCallback("face")

        elif (name == "BLOB"):
            self.state.blobs[value["color"]].posx = int(value["posx"])

            self.state.blobs[value["color"]].posy = int(value["posy"])

            self.state.blobs[value["color"]].size = int(value["size"])

            self.runCallback("blob")

        elif (name == "QRCODEAPPEAR"):

            self.state.qr = QRCode(float(value["coordx"]),
                             float(value["coordy"]),
                             float(value["distance"]),
                             float(value["p1x"]),
                             float(value["p1y"]),
                             float(value["p2x"]),
                             float(value["p2y"]),
                             float(value["p3x"]),
                             float(value["p3y"]),
                             value["id"])

            self.runCallback("qr")


        elif (name == "QRCODE"):
            self.state.qr = QRCode(float(value["coordx"]),
                             float(value["coordy"]),
                             float(value["distance"]),
                             float(value["p1x"]),
                             float(value["p1y"]),
                             float(value["p2x"]),
                             float(value["p2y"]),
                             float(value["p3x"]),
                             float(value["p3y"]),
                             value["id"])
            print(self.state.qr)


        elif (name == "QRCODELOST"):
            self.state.qr = QRCode(0, 0, 0, 0, 0, 0, 0, 0, 0, "None")



    def configureBlobTracking(self, red, green, blue, custom):
        name = "CONFIGURE-BLOBTRACKING"
        id = self.state.getId()
        values = {"red": red,
                  "green": green,
                  "blue": blue,
                  "custom": custom}

        return Message(name, values, id)


